from django import forms
from . models import Posts
STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['fname', 'sname', 'sex', 'amount']
        