from django.db import models

class Recipes(models.Model):
    title = models.CharField(max_length = 255, unique = True)
    description = models.CharField(max_length = 255, unique = True)
    slug = models.SlugField()
    preparation_time = models.IntegerField
    preparation_time_unit = models.CharField(max_length = 65)
    servings = models.IntegerField
    servings_unit = models.CharField(max_length = 65)
    preparation_steps = models.TextField
    preparation_steps_is_html = models.BooleanField(default=False)
    #esses campos servi para registra as datas
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    
    
                        
    
    
    
# Create your models here.
