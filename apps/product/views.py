from django.utils.translation import gettext as _
from rest_framework import authentication, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.product.models import Favorite, Product
from apps.product.serializers import FavoriteSerializer, ProductSerializer


class NotFound(Response):
    def __init__(self, message):
        super().__init__(
            data={"message": message}, status=status.HTTP_404_NOT_FOUND
        )


class ProductView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    model = Product
    name = model._meta.verbose_name.title()
    serializer = ProductSerializer

    def delete(self, request, product_id):
        queryset = self.model.objects.filter(id=product_id).first()
        if queryset:
            serializer = self.serializer(queryset)
            queryset.delete()
            return Response(serializer.data)
        else:
            return NotFound(_(f'{self.name} not found'))

    def get(self, request, product_id=None):
        queryset = (
            self.model.objects.filter(id=product_id)
            if product_id
            else self.model.objects.all()
        )
        if queryset:
            serializer = self.serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return NotFound(_(f'{self.name} not found'))

    def post(self, request):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def put(self, request, product_id):
        queryset = self.model.objects.filter(id=product_id).first()
        if queryset:
            serializer = self.serializer(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return NotFound(_(f'{self.name} not found'))


class FavoriteView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    model = Favorite
    name = model._meta.verbose_name.title()
    serializer = FavoriteSerializer

    def delete(self, request, favorite_id):
        queryset = self.model.objects.filter(id=favorite_id).first()
        if queryset:
            serializer = self.serializer(queryset)
            queryset.delete()
            return Response(serializer.data)
        else:
            return NotFound(_(f'{self.name} not found'))

    def get(self, request, favorite_id=None):
        queryset = (
            self.model.objects.filter(id=favorite_id)
            if favorite_id
            else self.model.objects.all()
        )
        if queryset:
            serializer = self.serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return NotFound(_(f'{self.name} not found'))

    def post(self, request):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
