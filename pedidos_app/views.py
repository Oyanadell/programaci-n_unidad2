from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pedidos_app.models import Cliente, Categoria

from pedidos_app.serializers import ClienteSerializer, CategoriaSerializer


#CLIENTE
@api_view(['POST','PUT'])
def crear_cliente(request):
    datos_cliente_deserializado = ClienteSerializer(data=request.data)

    if datos_cliente_deserializado.is_valid(): # Validar básico
        datos_cliente_deserializado.save() # Guardar
        return Response(datos_cliente_deserializado.data, status=status.HTTP_201_CREATED)
    else:
        return Response(datos_cliente_deserializado.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def listar_clientes(request):
    try:
        listado_clientes = Cliente.objects.all()
        serializado = ClienteSerializer(listado_clientes, many=True)

        return Response(serializado.data, status=status.HTTP_200_OK)

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST) 
    
@api_view(['GET'])
def listar_cliente(request, id):
    try: 
        cliente_obtenido = Cliente.objects.get(id=id)
        serializado = ClienteSerializer(cliente_obtenido, many=False)

        return Response(serializado.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
def modificar_cliente(request):
    try:
        cliente_seleccionado = Cliente.objects.get(id=id)
        serializado = ClienteSerializer(cliente_seleccionado, data=request.data)

        if serializado.is_valid():
            cliente_seleccionado.save()
            return Response(serializado.data, status=status.HTTP_202_ACCEPTED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_cliente(request, id):
    try:
        cliente_obtenido = Cliente.objects.get(id=id)
        cliente_obtenido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


    

#CATEGORIA
@api_view(['POST','PUT'])
def crear_categoria(request):
    datos_categoria_deserializado = CategoriaSerializer(data=request.data)

    if datos_categoria_deserializado.is_valid(): # Validar básico
        datos_categoria_deserializado.save() # Guardar
        return Response(datos_categoria_deserializado.data, status=status.HTTP_201_CREATED)
    else:
        return Response(datos_categoria_deserializado.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def listar_categorias(request):
    try:
        listado_categorias = Categoria.objects.all()
        serializado = CategoriaSerializer(listado_categorias, many=True)

        return Response(serializado.data, status=status.HTTP_200_OK)

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST) 
    
@api_view(['GET'])
def listar_categoria(request, id):
    try: 
        categoria_obtenida = Categoria.objects.get(id=id)
        serializado = CategoriaSerializer(categoria_obtenida, many=False)

        return Response(serializado.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PATCH'])
def modificar_categoria(request, id):
    try:
        categoria_seleccionada = Categoria.objects.get(id=id)
        serializado = CategoriaSerializer(categoria_seleccionada, data=request.data)

        if serializado.is_valid():
            categoria_seleccionada.save()
            return Response(serializado.data, status=status.HTTP_202_ACCEPTED)
    except: 
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_categoria(request, id):
    try:
        categoria_seleccionada = Categoria.objects.get(id=id)
        categoria_seleccionada.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)