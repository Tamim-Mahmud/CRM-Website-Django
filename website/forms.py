from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email=forms.EmailField(label='',widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'Your Email'}))
    first_name=forms.CharField(label='',max_length="50",widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}))
    last_name=forms.CharField(label='',max_length="50",widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}))
    # The Meta class provides metadata for the form, specifying the model (User) and the fields to include in the form.
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    #  __init__ method is used to  to customize the form fields css.
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password must contain at least 8 characters.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control', 'label': ''}),
    )
    
    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control', 'label':''}),
    )
    
    email = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'label': ''}),
    )
    
    phone = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control', 'label': ''}),
    )
    
    address = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control', 'label': ''}),
    )
    
    city = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control', 'label': ''}),
    )
    
    state = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'State', 'class': 'form-control', 'label': ''}),
    )
    
    zipcode = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Zip Code', 'class': 'form-control', 'label': ''}),
    )
    
    class Meta:
        model=Record
        exclude=('user',)
        