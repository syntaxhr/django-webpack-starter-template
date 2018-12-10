from django import forms

from posts.models import Post


class PostWizardForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = []
