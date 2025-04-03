from django.db import models

class MyImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')  # 실제 /media/uploads/ 경로 아래 저장
    analysis_text = models.TextField(blank=True, null=True)  # Gemini 분석 결과
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.created_at}"

class Gemini2(models.Model):
    objects = None
    name = models.CharField(max_length=15)
    explain = models.TextField()
    aiexplain = models.TextField()
    filename = models.CharField(max_length=100)
    file = models.FileField(upload_to='gemini/')  # 실제 /media/uploads/ 경로 아래 저장
    today = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}_{self.filename}"
class ChatGpt(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    explain = models.TextField()
    aiexplain = models.TextField()

    file = models.FileField(upload_to='chatgpt/')  # 실제 /media/uploads/ 경로 아래 저장
    today = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}_{self.file}"


