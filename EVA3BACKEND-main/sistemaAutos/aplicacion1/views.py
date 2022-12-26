from django.shortcuts import render
from .serializers import ClienteSerializer
from .models import Cliente
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET', 'POST'])
def cliente_list(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        serializer =ClienteSerializer(clientes, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ClienteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT', 'DELETE'])
def clientes_detail(request, pk):
    try:
        clientes = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ClienteSerializer(clientes)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ClienteSerializer(clientes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        clientes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)