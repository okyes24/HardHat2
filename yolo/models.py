from django.db import models

# Create your models here.
class Yolo(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    aiexplain = models.TextField()
    original_img = models.FileField(upload_to='yolo/original/')  # 실제 /media/uploads/ 경로 아래 저장
    result_img = models.FileField(upload_to='yolo/result/')  # 실제 /media/uploads/ 경로 아래 저장
    today = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}_{self.today}"