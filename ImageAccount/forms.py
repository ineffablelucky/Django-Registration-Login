from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegisterationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
            )

    def save(self, commit=True):
        user = super(RegisterationForm,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

    
    
class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['password'].help_text = self.fields['password'].help_text.format('../password/')
        f = self.fields.get('user_permissions')
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')
