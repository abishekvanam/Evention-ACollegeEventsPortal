from django import forms

class QuestionForm(forms.Form):
    question_text=forms.CharField(max_length=300)

