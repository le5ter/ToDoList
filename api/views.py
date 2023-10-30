from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import TaskSerializer
from base.models import Task


class TaskView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        user_id = self.request.user.id
        if user_id:
            return Task.objects.filter(user_id=user_id)
        else:
            return Task.objects.filter(user_id=0)

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.user.id)
        return serializer.save(user=user)


class SingleTaskView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
