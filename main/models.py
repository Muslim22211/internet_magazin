from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name

class Predmet(models.Model):
    name = models.CharField('Название',max_length=250)
    price = models.FloatField('Цена')
    img = models.ImageField('Фото', upload_to='imgs/')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    description = models.TextField('Описание')
                                              
    

    def __str__(self):  
                      
        return self.name

