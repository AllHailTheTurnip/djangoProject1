from django import forms
import psycopg2


class Post(forms.Form):
    message = forms.CharField(max_length=255)



