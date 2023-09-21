from django.db import models


class Product(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Lesson(models.Model):
    products = models.ManyToManyField(Product, related_name='lessons')
    title = models.CharField(max_length=255)
    video_link = models.URLField()
    duration_seconds = models.IntegerField()


class UserLessonAccess(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
    viewed_duration_seconds = models.IntegerField(default=0)
    lesson_duration_seconds = models.IntegerField()

    def mark_as_viewed(self):
        if (self.viewed_duration_seconds / self.lesson_duration_seconds) >= 0.8:
            self.viewed = True
        else:
            self.viewed = False
