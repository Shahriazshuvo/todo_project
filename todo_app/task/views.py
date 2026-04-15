from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Task


class CustomLoginView(LoginView):
    template_name = "task/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")

class TaskList(ListView):
    model = Task
    context_object_name = "tasks"
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)

        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["tasks"] = context["tasks"].filter(title__contains=search_input)
        
        context["search_input"] = search_input
        return context
    

class TaskCreate(CreateView):
    model = Task
    fields = ["title", "description", "completed", "due_date"]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    
class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "task/task_detail.html"

class TaskUpdate(UpdateView):
    model = Task
    fields = ["title", "description", "completed", "due_date"]
    success_url = reverse_lazy("tasks")

class DeleteView(DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)
