from django.db import models

class Room(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return str(self.name)

class Food(models.Model):
    name = models.CharField(max_length = 200)
    desc = models.TextField(null = True, blank = True)
    def __str___(self):
        return self.name
