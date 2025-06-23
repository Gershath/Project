from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User  # This now refers to your CustomUser
#         fields = ('username', 'password1', 'password2')

#     def __init__(self, *args, **kwargs):
#         super(CustomUserCreationForm, self).__init__(*args, **kwargs)
#         for fieldname in ['username', 'password1', 'password2']:
#             self.fields[fieldname].help_text = None
#             self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
 # Add bootstrap class






class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email
