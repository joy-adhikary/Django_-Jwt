from django.db import models

POSITION = (
    ('frontend', 'frontend'),
    ('fullstack', 'fullstack'),
    ('backend', 'backend'),
)

class Emp(models.Model):
    name = models.CharField(max_length=512, blank=False),
    description = models.CharField(max_length=512),
    created_on = models.DateTimeField(auto_now_add=True)


class EngEmp(models.Model):
    name = models.CharField(max_length=512)
    position = models.CharField(max_length=512, choices=POSITION, blank=False, default='backend'),
    salary = models.IntegerField()
