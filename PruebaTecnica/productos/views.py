from productos.serializers import serializersProducts, serializersProductsUpdate, ViewProductSerializers, serializersAllProducts
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from productos.models import Producto 

@api_view(['POST'])
def register_product(request):
     """
     Crea un usuario nuevo
     """
     if request.method == 'POST':
        serializer = serializersProducts(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def details_product(request, _id):
        """
        Recuperar, actualizar y registrar usuario
        """       
   
        try: 
            producto = Producto.objects.get(pk=_id)
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer =ViewProductSerializers(producto)
            return Response(serializer.data)
        elif request.method == 'PUT':
           serializer = serializersProductsUpdate(producto, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_products(request):
        try:
            products = Producto.objects.all()
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializersProductos =  serializersAllProducts(products, many=True)
            return Response({"allProducts": serializersProductos.data})

@api_view(['DELETE'])
def delete_product(request, _id):
        try:
            product = Producto.objects.get(pk=_id)
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'DELETE':
            product.delete()
            return Response({"message": "Producto eliminado"})

    


