from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Faq(models.Model):
    question = models.CharField(max_length=200)
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag, 'Tag', through='faq_tag')
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'
        
        ordering = ['-created_at']
        
        
class Faq_tag(models.Model):
    faq = models.ForeignKey(Faq, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Faq_detail(models.Model):
    
    class CodeType(models.TextChoices):
        HTML = 'html', 'HTML'
        CSS = 'css', 'CSS'
        JS = 'js', 'JavaScript'
        PYTHON = 'python', 'Python'
        DJANGO = 'django', 'Django'
        SQL = 'sql', 'SQL'
        SHELL = 'shell', 'Shell'
        BASH = 'bash', 'Bash'
        OTHER = 'other', 'Other'
        BLANK = '', 'Blank'
    
    faq = models.ForeignKey(Faq, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)
    code = models.TextField(blank=True, null=True)
    code_type = models.CharField(max_length=50, blank=True, null=True, choices=CodeType.choices, default=CodeType.BLANK)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = 'Detalle de Pregunta'
        verbose_name_plural = 'Detalles de Preguntas'
        
        ordering = ['order', '-created_at']
        
    def __str__(self):
        return self.title