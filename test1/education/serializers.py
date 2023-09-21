from rest_framework import serializers
from .models import Lesson, UserLessonAccess, Product


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class UserLessonAccessSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = UserLessonAccess
        fields = ['lesson', 'viewed', 'viewed_duration_seconds']


class ProductStatsSerializer(serializers.ModelSerializer):
    total_lessons_viewed = serializers.SerializerMethodField()
    total_time_watched = serializers.SerializerMethodField()
    total_students = serializers.SerializerMethodField()
    purchase_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'total_lessons_viewed', 'total_time_watched', 'total_students', 'purchase_percentage']

    def get_total_lessons_viewed(self, obj):
        # Рассчитайте количество просмотренных уроков для данного продукта
        return obj.lessons.filter(userlessonaccess__viewed=True).count()

    def get_total_time_watched(self, obj):
        # Рассчитайте суммарное время просмотра для данного продукта
        return obj.lessons.filter(userlessonaccess__viewed=True).aggregate(total_time=models.Sum('userlessonaccess__viewed_duration_seconds'))['total_time'] or 0

    def get_total_students(self, obj):
        # Рассчитайте количество учеников для данного продукта
        return obj.owner.count()

    def get_purchase_percentage(self, obj):
        # Рассчитайте процент приобретения продукта
        total_users = User.objects.count()  # Предполагается, что User - это модель пользователей
        if total_users > 0:
            return (obj.owner.count() / total_users) * 100
        else:
            return 0
