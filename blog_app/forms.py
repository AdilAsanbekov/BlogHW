from django.forms.widgets import HiddenInput
from .models import Comment, UserLike, UserDislike
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {'comment': HiddenInput()}

class LikeForm(forms.ModelForm):
    class Meta:
        model = UserLike
        fields = ()
        widgets = {'post': HiddenInput()}

class DislikeForm(forms.ModelForm):
    class Meta:
        model = UserDislike
        fields = ()
        widgets = {'post': HiddenInput()}