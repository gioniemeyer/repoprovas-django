from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Professor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=6)

    def __str__(self):
        return self.category


class Test(models.Model):
    semester = models.CharField(max_length=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    file = models.CharField(max_length=200)

    def publish(self):
        self.save()
