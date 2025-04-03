from django.contrib import admin

from llm.models import Gemini2, ChatGpt


# Register your models here.
@admin.register(Gemini2)
class  GeminiAdmin(admin.ModelAdmin):
    pass

@admin.register(ChatGpt)
class  ChatGptAdmin(admin.ModelAdmin):
    pass