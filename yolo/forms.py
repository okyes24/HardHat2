from django import forms

from llm.models import Gemini2, ChatGpt
from yolo.models import Yolo


class YoloForm(forms.ModelForm):
    class Meta:
        model = Yolo
        #fields = ['title', 'name', 'content']
        exclude=['today']

