from django import forms
from .models import Post
from groups.models import Group

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['group'].queryset = Group.objects.all().filter(members=self.request.user)

    class Meta():
        fields = ('message', 'group')
        model = Post
