from .filters import TaskFilter
from rest_framework import viewsets ,generics ,permissions ,filters
from .serializers import TaskSerializer
from .models import Task
from .permissions import IsOwnerOrReadOnly


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['due_date', 'status']  # Define fields for sorting
    search_fields = ['title', 'description', 'due_date']  # Define fields for searching
    filterset_class = TaskFilter
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]




