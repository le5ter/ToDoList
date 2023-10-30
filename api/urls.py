from django.urls import path

from .views import TaskView, SingleTaskView

urlpatterns = [
    path("tasks/", TaskView.as_view()),
    path("tasks/<int:pk>", SingleTaskView.as_view())
]
