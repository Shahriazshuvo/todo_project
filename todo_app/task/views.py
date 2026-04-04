from django.views.generic import ListView
from .models import Task


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
    
