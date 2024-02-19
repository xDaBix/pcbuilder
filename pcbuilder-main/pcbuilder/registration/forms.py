from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')  # Adjust fields as needed
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_password2(self):
        # Ensure passwords match
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password-repeat')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match')
        return password2
