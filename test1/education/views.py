from rest_framework import generics
from .models import UserLessonAccess, Product
from .serializers import UserLessonAccessSerializer, ProductStatsSerializer


class UserLessonAccessList(generics.ListAPIView):
    serializer_class = UserLessonAccessSerializer

    def get_queryset(self):
        user = self.request.user
        # Получите все записи о доступе пользователя к урокам
        return UserLessonAccess.objects.filter(user=user)


class ProductLessonAccessList(generics.ListAPIView):
    serializer_class = UserLessonAccessSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']  # Получаем ID продукта из URL
        # Получите все записи о доступе пользователя к урокам данного продукта
        return UserLessonAccess.objects.filter(user=user, lesson__products=product_id)


class ProductStatsList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductStatsSerializer
