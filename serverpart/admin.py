from django.contrib import admin

# Register your models here.
from .models import TaskKeys, Tasks, SolvedTasks


admin.site.register(TaskKeys)

admin.site.register(Tasks)

admin.site.register(SolvedTasks)