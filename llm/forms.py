from django import forms

from llm.models import Gemini2, ChatGpt


class GeminiForm(forms.ModelForm):
    class Meta:
        model = Gemini2
        #fields = ['title', 'name', 'content']
        exclude=['today']

class ChatGptForm(forms.ModelForm):
    class Meta:
        model = ChatGpt
        #fields = ['title', 'name', 'content']
        exclude=['today']