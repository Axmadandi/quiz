from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Answers)
admin.site.register(Quizzes)

@admin.register(Ways)
class WaysAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}