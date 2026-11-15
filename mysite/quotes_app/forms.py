from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .mongo_models import Authors

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AuthorForm(forms.Form):
    fullname = forms.CharField(max_length=100)
    born_date = forms.CharField(max_length=100)
    born_location = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)


class QuoteForm(forms.Form):
    quote = forms.CharField(widget=forms.Textarea)
    author = forms.ChoiceField()
    tags = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        authors = Authors.objects.all()

        self.fields['author'].choices = [
            (str(author.id), author.fullname)
            for author in authors
        ]