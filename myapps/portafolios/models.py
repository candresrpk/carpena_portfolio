from django.db import models
from django.utils.text import slugify
import uuid

# Create your models here.


class tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['-created_at']

class Portafolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='portafolio/images/')
    git_url = models.URLField(blank=True)
    tag = models.ManyToManyField(tag, 'Tag', through='PortafolioTag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
                    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + str(uuid.uuid4()[:4]))
        super().save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
    
    
    class Meta:
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolios'
        
        ordering = ['-created_at']
        
        
    
class PortafolioTag(models.Model):
    portafolio = models.ForeignKey(Portafolio, on_delete=models.CASCADE)
    tag = models.ForeignKey(tag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    