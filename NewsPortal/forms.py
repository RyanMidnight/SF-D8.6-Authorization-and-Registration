from django import forms
from django.core.exceptions import ValidationError
from .models import Post
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'category',
            'headline',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        headline = cleaned_data.get('headline')
        if headline is not None and len(headline) > 255:
            raise ValidationError({
                'headline': 'Headline cannot be longer than 255 symbols.'
            })
        return cleaned_data


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='Common')
        common_group.user_set.add(user)
        return user
