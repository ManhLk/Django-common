from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to="uploads/%Y/%m")


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name


class ItemBase(models.Model):
    subjects = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to="upload_to/%Y/%m", default=None)
    create_date  = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True



class Course(ItemBase):
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.subjects, self.description, self.category

    class Meta:
        unique_together = ("subjects", "category")



class Lesson(ItemBase):
    image = models.ImageField(upload_to="courses/%Y/%m")
    active  = models.BooleanField(default=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("subjects", "course")
