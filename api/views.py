from rest_framework import viewsets

from .serializers import GameUnitSerializer
from .models import GameUnit


class GameUnitViewSet(viewsets.ModelViewSet):
    queryset = GameUnit.objects.all().order_by('name')
    serializer_class = GameUnitSerializer
