from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    # These are the extra fields that will show up on the Signup Page
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    enrollment_number = forms.CharField(max_length=20, label='Enrollment Number', widget=forms.TextInput(attrs={'placeholder': 'e.g., 001123456'}))
    course_and_shift = forms.CharField(max_length=100, label='Course & Shift', widget=forms.TextInput(attrs={'placeholder': 'e.g., BBA Morning'}))
    college = forms.CharField(max_length=150, label='College', widget=forms.TextInput(attrs={'placeholder': 'Your College Name'}))

    def save(self, request):
        # 1. Save the default user (email/password)
        user = super(CustomSignupForm, self).save(request)
        
        # 2. Add our custom data to the user object
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.enrollment_number = self.cleaned_data['enrollment_number']
        user.course_and_shift = self.cleaned_data['course_and_shift']
        user.college = self.cleaned_data['college']
        
        # 3. Save again to database
        user.save()
        return user