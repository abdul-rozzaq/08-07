from django.contrib import admin

from .models import Course, Lesson, User

admin.site.register([Course, Lesson, User])
