from django.db import models
from django.utils.text import slugify
import uuid

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['-created_at']

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='projects/')
    git_url = models.URLField(blank=True)
    tag = models.ManyToManyField(Tag, 'Tag', through='ProjectTag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
                    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + str(uuid.uuid4())[:4])
        super().save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
    
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        
        ordering = ['-created_at']
        
        
    
class ProjectTag(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class ProjectDetail(models.Model):
    
    TIPO_CHOICES = (
        ('texto', 'Texto'),
        ('imagen', 'Imagen'),
    )
    
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    texto = models.TextField()
    image = models.ImageField(upload_to='portafolio/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    portafolio = models.ForeignKey(Project, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Detalle de Proyecto'
        verbose_name_plural = 'Detalles de Proyectos'
        ordering = ['order']
        
    
    