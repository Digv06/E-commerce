from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=75)
    category = models.CharField(max_length=100,default='')
    subcategory = models.CharField(max_length=200,default='')
    price = models.IntegerField(default=0)
    desc= models.CharField(max_length=200)
    pub_date=models.DateField()
    image = models.ImageField(upload_to='shop/images',default='')

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30,default='')
    phone = models.CharField(max_length=10,default='')
    desc = models.CharField(max_length=75,default='')

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items = models.CharField(max_length=10000)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=15 , default="")
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zip=models.CharField(max_length=10)

class UpdateOrder(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:10] + "..."