from django.urls import path
from llm.views import gemini_txt, novel_txt, gemini_img, gemini_delete, alibaba_api, chatgpt_api, chatgpt_api_img, \
    chatgpt_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('gemini_txt/', gemini_txt, name='gemini_txt'),
    path('novel_txt/', novel_txt, name='novel_txt'),
    path('gemini_img/', gemini_img, name='gemini_img'),
    path('gemini_delete/<int:pk>', gemini_delete, name='gemini_delete'),
    path('alibaba_api/', alibaba_api, name='alibaba_api'),
    path('chatgpt_api/', chatgpt_api, name='chatgpt_api'),
    path('chatgpt_api_img/', chatgpt_api_img, name='chatgpt_api_img'),
    path('chatgpt_delete/<int:pk>', chatgpt_delete, name='chatgpt_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)