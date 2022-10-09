from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=55)
    reg_date = models.DateField(auto_now_add=True)
    products_qty = models.PositiveIntegerField(default=0,editable=False)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriya"

    def __str__(self):
        return f"{self.name}  Added :{self.reg_date}"   


class Product(models.Model):
    category = models.ForeignKey(Category, db_index=True,  on_delete=models.PROTECT)
    name = models.CharField(verbose_name="Tovar nomi",help_text="dssdf sdjdsjfskdfsdfs dshfj", max_length=355,blank=True)
    text = models.TextField(verbose_name="Tovar xaqida",max_length=8000,default="Text yo'q")
    view = models.PositiveIntegerField(verbose_name="Ko'rishlar soni",default=0,editable=False )
    likes = models.PositiveIntegerField(default=0,editable=False)
    dislikes = models.PositiveIntegerField(default=0,editable=False)
    image = models.ImageField(upload_to="")
    reg_date = models.DateField(auto_now_add=True)
    tel_raqam=models.PositiveIntegerField(default=0,editable=True)
    

    class Meta:
        verbose_name = "Tovar"
        verbose_name_plural = "Tovarlar"

    def __str__(self):
        return self.name    
    
    def get_absolute_url(self):
        return reverse('car_detail', args=[str(self.id)])




class Comment(models.Model):
    article = models.ForeignKey(Product,on_delete=models.CASCADE)
    incomment = models.ForeignKey("Comment",on_delete=models.CASCADE,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    reg_date = models.DateField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)


