# itemDashboard/views.py

from .models import Item
from .serializers import ItemSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer
from .serializers import ItemCreateSerializer
from django.views.decorators.csrf import csrf_exempt

class ItemListAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Get query parameters from the request
        category = self.request.query_params.get('category', None)
        stock_status = self.request.query_params.get('stock_status', None)

        # Apply filters if query parameters are provided
        if category:
            queryset = queryset.filter(category=category)
        if stock_status:
            queryset = queryset.filter(stock_status=stock_status)

        return queryset

class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
   
class ItemCreateAPIView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemCreateSerializer
    
    @csrf_exempt 
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



