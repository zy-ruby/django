from models import *
from django import forms
from django.contrib.auth.models import User
from rufirst.models import *
from django.forms import ModelForm


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(max_length=20,
                               label='Password',
                               widget = forms.PasswordInput(),
                                required=True)

    password2 = forms.CharField(max_length=20,
                                label='Confirm Password',
                                widget=forms.PasswordInput(),
                                required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        print "password2"
        print password2
        if password2 != password1:
            print password1
            print password2
            raise forms.ValidationError("Passwords did not match.")
        # if not password1 or not password2:
        #     raise forms.ValidationError("You must enter a password")
        if len(password2)<2:
            raise forms.ValidationError("Password must be at least 2 characters")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username):
            raise forms.ValidationError("username has already been taken")
        return username

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['photo','age','bio']

    def save(self, commit= True):
        profile = super(EditProfileForm, self).save(commit=False)
        profile.bio = self.cleaned_data['bio']
        profile.age = self.cleaned_data['age']
        if commit:
            profile.save()
        return profile


