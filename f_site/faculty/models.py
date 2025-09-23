from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="specialities")

    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name="disciplines")

    def __str__(self):
        return self.name


class Professor(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="professors")

    def __str__(self):
        return self.name


class Home(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name