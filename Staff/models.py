from django.db import models

# Create your models here.       


class employee(models.Model):
    sex = [
        ['1', '男'],
        ['2', '女'],
       
    ]

    level = [
        ['1', '總經理'],
        ['2', '主管'],
        ['3', '員工'],
    ]


    name = models.CharField(max_length=32,verbose_name='姓名')

    email = models.EmailField(verbose_name='郵箱')

    dep = models.ForeignKey(to="department", on_delete=models.CASCADE)

    group = models.ManyToManyField(to="group")

    salary = models.DecimalField(max_digits=8, decimal_places=2)    

    phone = models.CharField(max_length=11)

    address = models.CharField(max_length=50)

    gender = models.CharField(max_length=1, choices=sex, verbose_name="性別")

    head_img = models.ImageField(upload_to='headimage', blank=True, null=True, verbose_name="相片")

    attachment = models.FileField(upload_to='filedir', blank=True, null=True, verbose_name="附件")

    hierarchy = models.CharField(max_length=1, choices=level, verbose_name="階級")
    


class department(models.Model):

    dep_name = models.CharField(max_length=32, verbose_name="部門名稱")

    dep_script = models.CharField(max_length=60, verbose_name="備註")


class group(models.Model):

    group_name = models.CharField(max_length=32, verbose_name="社團名稱")

    group_script = models.CharField(max_length=60, verbose_name="備註")

