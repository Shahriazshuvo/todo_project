from django.contrib import path
from .views import TaskList, TaskCreate, TaskDetail, TaskUpdate, DeleteView

urlpatterns = [
    path("",TaskList.as_view(), name="tasks"),
    path("task-create/", TaskCreate.as_view(), name="task-create"),
    path("task/<int:pk>", TaskDetail.as_view(), name="task-detail"),
    path("task-update/<int:pk>", TaskUpdate.as_view(), name="task-update"),
    path("task-delete/<int:pk>", DeleteView.as_view(), name="task-delete"),
]