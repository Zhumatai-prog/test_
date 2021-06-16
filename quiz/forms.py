from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from . import models


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class TopicForm(forms.ModelForm):
    class Meta:
        model=models.Topic
        fields=['topic_name']


class QuestionForm(forms.ModelForm):

    #this will show dropdown __str__ method course model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in course model and return it
    topicID=forms.ModelChoiceField(queryset=models.Topic.objects.all(),empty_label="Topic Name", to_field_name="id")
    class Meta:
        model=models.Question
        fields=['question','option1','option2','option3','option4','answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }


#class QuestionUpdateForm(forms.ModelForm):
#    class Meta:
#        model = models.Question
#        fields = ['entry']


class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

#class StudentForm(forms.ModelForm):
#    class Meta:
#        model=models.Student
#        fields=['address','mobile','profile_pic']
