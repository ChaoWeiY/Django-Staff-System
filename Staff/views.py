from django.shortcuts import render, redirect
from Staff.models import employee, department, group
# Create your views here.


def list_dep(request):
    dep_list = department.objects.all()
    return render(request, "list_dep.html", locals())


def add_dep(request):
    if request.method == "POST":
        dep_name = request.POST.get('dep_name')
        dep_script = request.POST.get("dep_script")
        if dep_name.strip() == '' :
            error_info = "部門名稱不能為空!"            
            return render(request, "add_dep.html", locals())

        try:
            p = department.objects.create(dep_name=dep_name, dep_script=dep_script)
            return redirect('/list_dep/')
        except Exception as e :
            error_info = "輸入部門名稱重複或信息有錯誤!"           
            return render(request, "add_dep.html", locals())
        
        finally :
            pass
   
    return render(request, "add_dep.html", locals())


def del_dep(request, dep_id):
    dep_object = department.objects.get(id=dep_id)
    dep_object.delete()
    return redirect("/list_dep/")


def edit_dep(request,dep_id):
    if request.method == "POST":
        id = request.POST.get("id")
        dep_name = request.POST.get("dep_name")
        dep_script = request.POST.get("dep_script")
        dep_object = department.objects.get(id=id)
        dep_object.dep_name = dep_name
        dep_object.dep_script = dep_script
        dep_object.save()
        return redirect("/list_dep/")
    else:
        dep_object = department.objects.get(id=dep_id)        
        return render(request, "edit_dep.html", locals())




def list_group(request):
    group_list = group.objects.all()   
    return render(request, "list_group.html", locals())


def add_group(request):
    if request.method == "POST":
        group_name = request.POST.get('group_name')
        group_script = request.POST.get("group_script")
        if group_name.strip() == '' :
            error_info = "團體名稱不能為空!"            
            return render(request, "add_group.html", locals())

        try:
            group.objects.create(group_name=group_name, group_script=group_script)
            return redirect('/list_group/')
        except Exception as e :
            error_info = "輸入團體名稱重複或信息有錯誤!"            
            return render(request, "add_group.html", locals())
        
        finally :
            pass

    return render(request, "add_group.html", locals())


def del_group(request, group_id):
    group_object = group.objects.get(id=group_id)
    group_object.delete()
    return redirect("/list_group/")



def edit_group(request,group_id):
    if request.method == "POST":
        id = request.POST.get("id")
        group_name = request.POST.get("group_name")
        group_script = request.POST.get("group_script")
        group_object = group.objects.get(id=id)
        group_object.group_name = group_name
        group_object.group_script = group_script
        group_object.save()
        return redirect("/list_group/")
    else:
        group_object = group.objects.get(id=group_id)        
        return render(request, "edit_group.html", locals())


def list_employee(request):
    emp_list = employee.objects.all()    
    return render(request, "list_employee.html", locals())

def delete_employee(request, emp_id):
    emp = employee.objects.get(id=emp_id)
    emp.delete()
    return redirect("/list_employee/")

def add_employee(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        dep = request.POST.get("dep")        
        salary = request.POST.get("salary")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")
        head_img = request.FILES.get("head_img")
        attachment = request.FILES.get("attachment")
        hierarchy = request.POST.get("hierarchy")
        address = request.POST.get("address")       
        groups = request.POST.getlist("group")
        new_emp = employee.objects.create(name=name, email=email, salary=salary, dep_id=dep, phone=phone, gender=gender, head_img=head_img, attachment=attachment, address=address, hierarchy=hierarchy)        
        new_emp.group.set(groups)
        return redirect("/list_employee/")
    emp_list = employee.objects.all()
    dep_list = department.objects.all()
    group_list = group.objects.all()    
    return render(request, "add_employee.html", locals())

def edit_employee(request, emp_id):
    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        dep = request.POST.get("dep")   
        groups = request.POST.get("group")
        gender = request.POST.get("gender")
        head_img = request.FILES.get("head_img")
        attachment = request.FILES.get("attachment")
        hierarchy = request.POST.get("hierarchy")
        emp = employee.objects.get(id=id)
        emp.name = name
        emp.email = email
        emp.dep_id = dep       
        emp.gender = gender
        emp.hierarchy = hierarchy
        emp.group.set(groups)
        if head_img :
            emp.head_img = head_img
        if attachment:
            emp.attachment=attachment
        emp.save()
        return redirect("/list_employee/")
    emp = employee.objects.get(id=emp_id)
    dep_list = department.objects.all()
    group_list = group.objects.all()   
    return render(request, "edit_employee.html", locals())

def index(request):
    emp_list = employee.objects.all()    
    return render(request, "list_employee.html", locals())
    