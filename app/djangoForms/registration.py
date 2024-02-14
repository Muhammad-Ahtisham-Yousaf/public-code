from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms 


# menually
# from django import forms 
# from..models import User

class CustomRegistrationForm (UserCreationForm):
    full_name = forms.CharField( max_length=100,  widget= forms.TextInput( attrs={ 'class':'','placeholder':' DFull Name'  }) )
    spacialization = forms.CharField (max_length=200,  widget= forms.TextInput( attrs={ 'class':'','placeholder':'Dspecialization'  }))
    
    # username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'','placeholder':'DUsername'  }) )
    email = forms.EmailField( widget=forms.TextInput(attrs={'class':'','placeholder':'DEmail'}))
    contact_no = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'','placeholder':'DContact #'}))
    # CV = forms.FileField( widget=forms.FileInput(attrs= {'class':''}) )
    
    
    class Meta:
        model = User
        fields = [ 'id','full_name','username','email','password1', 'password2','contact_no','spacialization']
        # fields = ('__all__')
        # exclude = ('id') 

    def __init__(self, *args, **kwargs):
        super(CustomRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].widget.attrs['class'] = ''
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['class'] = ''  # Add class here
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].widget.attrs['class'] = ''  # Add class here
