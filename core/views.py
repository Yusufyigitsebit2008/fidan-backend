from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import School, InventoryItem, Request
from .serializers import SchoolSerializer, InventoryItemSerializer, RequestSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        try:
            school = School.objects.get(user=user)
            serializer = self.get_serializer(school)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "Bu kullanıcıya bağlı bir okul profili yok!"}, status=404)

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer