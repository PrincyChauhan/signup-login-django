from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signupform(UserCreationForm):
    ROOM_CHOICES = (
        ('AC', 'AC'),
        ('NON-AC', 'NON-AC')
    )
    FOOD_CHOICES = (
            ('food', 'Food'),
            ('not-food', 'Not Food')
    )

    first_name=forms.CharField(max_length=30,required=False,help_text='required')
    last_name=forms.CharField(max_length=30,required=False,help_text='required')
    father_name=forms.CharField(max_length=30,required=False,help_text='required')
    mother_name=forms.CharField(max_length=30,required=False,help_text='required')
    address=forms.CharField(max_length=30,required=False,help_text='required')
    college_id=forms.CharField(max_length=30,required=False,help_text='required')
    email=forms.CharField(max_length=30,required=False,help_text='required')
    room_type = forms.ChoiceField(choices=ROOM_CHOICES, widget=forms.RadioSelect)
    food_preference = forms.ChoiceField(choices=FOOD_CHOICES, widget=forms.RadioSelect)

    
    class Meta:
        model=User
        fields=('username','first_name','last_name','father_name','mother_name','address','college_id','email','password1','password2')
        
    def save(self,commit=True):
        user=super(signupform,self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.father_name=self.cleaned_data['father_name']
        user.mother_name=self.cleaned_data['mother_name']
        user.address=self.cleaned_data['address']
        user.college_id=self.cleaned_data['college_id']
        user.email=self.cleaned_data['email']
        user.password=self.cleaned_data['password']
        user.room_type = self.cleaned_data['room_type']
        user.food_preference = self.cleaned_data['food_preference']
        
        if commit:
            user.save()
        return user