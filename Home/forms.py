from django.contrib.auth.forms import UserCreationForm
from .models import User

from .models import Idcard
from django import forms

CHOICES = [
    ('Chitwan', 'Chitwan'), ('Kathmandu', 'Kathmandu'),
    ('Bhaktapur', 'Bhaktapur'), ('Lalitpur', 'Lalitpur'), ]
gen = [('Male', 'Male'), ('Female', 'Female'),
       ('Others', 'Others'), ]
stat = [('Married', 'Married'), ('Single', 'Single'),
        ('Divorce', 'Divorce'), ]
Edu_level = [('Uneducated', 'Uneducated'), ('Slc', 'Slc'), ('Plus_2', 'Plus 2'),
             ('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('PHDs', 'PHDs'), ]
prof = [('Others', 'Others'), ('Service', 'Service'), ('Doctor', 'Doctor'), ('Framer', 'Framer'),
        ('Teacher', 'Teacher'), ('Social', 'Social Worker'), ('Lawyer', 'Lawyer'), ('Businessman', 'Businessman')]
CasteChoice = [('Others', 'Others'), ('Chettri', 'Chettri'), ('Brahmin', 'Brahmin'), ('Newar', 'Newar'),
               ('Thakuri', 'Thakuri')]
Reli = [('Others', 'Others'), ('Hindu', 'Hindu'), ('Buddha', 'Buddha'), ('Islam', 'Islam'),
        ('Christian', 'Christian')]


class card(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Enter Firstname'}))
    middlename = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Enter middlename'}))
    lastname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Enter lastname'}))
    dob = forms.DateField(widget=forms.NumberInput(
        attrs={'class': 'form-control my-2', 'type': 'date', 'Placeholder': 'Enter Date'}))
    birthplace = forms.ChoiceField(choices=CHOICES, widget=forms.Select(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Choose Birthplace'}))
    citizenship_no = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Enter Citizenship Number'}))
    issue_zone = forms.ChoiceField(label='Zone', choices=CHOICES, widget=forms.Select(
        attrs={'class': 'form-control my-2', 'Placeholder': 'enter zone'}))
    # issue_date = forms.DateField(widget=forms.DateInput(
    #     attrs={'class': 'form-control my-2', 'Placeholder': 'enter issue_date'}))

    gender = forms.ChoiceField(label='Gender',  choices=gen, widget=forms.Select(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Choose gender'}))

    marital_status = forms.ChoiceField(choices=stat, widget=forms.Select(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Choose Marital State'}))

    education = forms.ChoiceField(choices=Edu_level, widget=forms.Select(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Choose Education level'}))

    profession = forms.ChoiceField(choices=prof, widget=forms.Select(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Choose Profession'}))

    caste = forms.ChoiceField(choices=CasteChoice, widget=forms.Select(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Choose Caste'}))

    religion = forms.ChoiceField(choices=Reli, widget=forms.Select(
        attrs={'class': 'form-control my-2', 'Placeholder': 'Choose Caste'}))

    # def clean_dob(self):
    #     data = self.cleaned_data.get["dob"]
    #     if data == '':
    #         raise forms.ValidationError('Enter the date')
    #     return data

    class Meta:
        model = Idcard
        fields = ['firstname', 'middlename', 'lastname', 'dob', 'birthplace', 'citizenship_no',
                  'issue_zone', 'gender', 'marital_status', 'education', 'profession', 'caste', 'religion']


class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Enter Username'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Enter Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
