from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField('Category name', max_length=50)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categ')
    name = models.CharField('SubCategory name', max_length=50)
    slug = models.SlugField('SubCategory slug', unique=True)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
