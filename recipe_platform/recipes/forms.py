from django import forms
from django.contrib.auth import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        feilds = ['username', 'email', 'password1', 'password2']


from .models import Recipe
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description',
                'ingredients', 'instructions', 'cooking_time', 
                'difficulty', 'image']

