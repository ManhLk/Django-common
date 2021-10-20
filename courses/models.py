from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from ckeditor.fields import RichTextField

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to = "avatar/%Y/%m")

class Category(models.Model):
    name = models.CharField(max_length=250, null= False)

    def __str__(self):
        return self.name

class ItemBase(models.Model):
    subject = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to="upload/%Y/%m", default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['created_date']

class Course(ItemBase):
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
    
    class Meta:
        unique_together = ('subject', 'category')
    

class Lesson(ItemBase):
    content = RichTextField(null=True)
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, null=True, related_name='lessons')

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('subject', 'course')

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)