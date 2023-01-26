from django.db import models

# Create your models here.


class ProductsCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Products Category'
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)


class Products(models.Model):
    class Meta:
        verbose_name_plural = 'Products'
    name = models.CharField(max_length=100,blank=False,null=False,verbose_name="Specious Name")
    slug = models.SlugField(max_length=100,unique=True)
    category = models.ForeignKey(ProductsCategory,on_delete=models.SET_NULL,null=True)
    Photo1 = models.ImageField(upload_to='Products Photos',blank=True,null=True)
    Photo2 = models.ImageField(upload_to='Products Photos',blank=True,null=True) 
    Photo3 = models.ImageField(upload_to='Products Photos',blank=True,null=True)

