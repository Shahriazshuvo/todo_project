from django.contrib import path
from .views import CustomLoginView, RegisterPage, TaskList, TaskCreate, TaskDetail, TaskUpdate, DeleteView

urlpatterns = [
    path("",TaskList.as_view(), name="tasks"),
    path("task-create/", TaskCreate.as_view(), name="task-create"),
    path("task/<int:pk>", TaskDetail.as_view(), name="task-detail"),
    path("task-update/<int:pk>", TaskUpdate.as_view(), name="task-update"),
    path("task-delete/<int:pk>", DeleteView.as_view(), name="task-delete"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", RegisterPage.as_view(), name="register"),
]