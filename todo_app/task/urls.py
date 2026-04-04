from django.contrib import path
from .views import TaskList, TaskCreate

urlpatterns = [
    path("",TaskList.as_view(), name="tasks"),
    path("task-create/", TaskCreate.as_view(), name="task-create"),
]