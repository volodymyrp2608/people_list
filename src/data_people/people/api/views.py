from django.db.models import Q
from rest_framework import generics, mixins
from people.models import List_People
from .permissions import IsOwnerOrReadOnly
from .serializers import ListPeopleSerializer


class DataPeopleAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ListPeopleSerializer

    def get_queryset(self):
        qs = List_People.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(surname=query)|
                Q(name=query)
                ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}



class DataPeopleRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ListPeopleSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return List_People.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}
