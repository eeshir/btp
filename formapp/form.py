from django import forms
from .models import NewModel


# class MyForm(forms.ModelForm):
#     class Meta:
#         model = NewModel
#         exclude = [f'q{i}' for i in range(1, 21)]  # Include the fields you want to include in the form

class NewForm(forms.ModelForm):
    class Meta:
        model = NewModel
        exclude = [f'q{i}' for i in range(1, 21)]  # Include the fields you want to include in the form
