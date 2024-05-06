from django.contrib import admin
from .models import Room, Food, SportCourse, Topic, Message, User

admin.site.register(Food)
admin.site.register(Room)
admin.site.register(SportCourse)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(User)
