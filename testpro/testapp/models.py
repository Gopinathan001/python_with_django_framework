from django.db import models

# Create your models here.

class Details(models.Model):
    id=models.AutoField(primary_key=True)
    bankname=models.CharField(max_length=20, default='')
    Accountnumber=models.CharField(max_length=20, default='')
    password=models.CharField(max_length=20, default='')
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15, default='')

def __str__(self):
    return "%s " %(self.ename)

class Meta:  
    db_table = "BankDetails"

    