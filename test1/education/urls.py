from django.urls import path
from .views import UserLessonAccessList, ProductLessonAccessList, ProductStatsList


urlpatterns = [
    path('user-lesson-access/', UserLessonAccessList.as_view(), name='user-lesson-access-list'),
    path('product-lesson-access/<int:product_id>/', ProductLessonAccessList.as_view(),
         name='product-lesson-access-list'),
    path('product-stats/', ProductStatsList.as_view(), name='product-stats-list'),

]




