from django import forms

from .models import Recipes


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['title', 'short_description', 'category', 'description', 'steps', 'time', 'thumbnail']
