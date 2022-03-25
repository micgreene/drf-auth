from rest_framework import generics
from .serializer import BirdSerializer
from .models import Bird
from .permissions import IsOwnerOrReadOnly

class BirdList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Bird.objects.all()
    serializer_class = BirdSerializer

class BirdDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Bird.objects.all()
    serializer_class = BirdSerializer
