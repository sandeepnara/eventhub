from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class SignupForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=CustomUser.Role.choices,
        widget=forms.RadioSelect,
        initial=CustomUser.Role.ATTENDEE,
    )
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ('username','email','role','password1','password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user