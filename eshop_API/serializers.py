
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from eshop_products.models import Product
from .views import ProductModelSerializer

# # # # # # # # # # # # # # # #
#   The All of Code in API    #
# # # # # # # # # # # # # # # #
#        200 OK               #
#      201 CREATED            #
#     400 BAD_REQUEST         #
#      401 NOT_FOUND          #
#      204 NO CONTENT         #
# # # # # # # # # # # # # # # #

# class GetAllAPI(APIView):
#     def get(self, request):
#         query = Product.objects.all()
#         serializers = ProductModelSerializer(query, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def GetAllAPI(request):
    if request.method == 'GET':
        query = Product.objects.all()
        serializers = ProductModelSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class GetFavAPI(APIView):
    def get(self, request):
        query = Product.objects.filter(active=True)
        serializers = ProductModelSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class UpdateFavData(APIView):
    # دادن اطلاعات
    def get(self, request, pk):
        # گرفتن آیدی محصول و پیدا کردن آن در کالکشن
        query = Product.objects.get(pk=pk)
        # متوالی کردن محصول
        serializer = ProductModelSerializer(query)
        # برگرداندن اطلاعات محصول مورد نظر و دادن کد 200
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ویرایش اطلاعات
    def put(self,request,pk):
        # گرفتن آیدی محصول و پیدا کردن آن در کالکشن
        query = Product.objects.get(pk=pk)
        # متوالی کردن محصول و گرفتن اطلاعات محصول از طریق پستمن برای تغییر
        serialzer = ProductModelSerializer(query, data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data , status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostData(APIView):

    def post(self,request):
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class SearchData(APIView):
    def get(self, request):
        search = request.GET.get('name')
        query = Product.objects.filter(title__icontains=search)
        serializer = ProductModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteData(APIView):
    def delete(self, request, pk):
        query = Product.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

