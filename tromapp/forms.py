from django import forms 
from tromapp.models import *


class LoginForm(forms.Form): 
    email = forms.EmailField(label='Email',)
    password = forms.CharField(label='Mot de passe', widget = forms.PasswordInput) 
  
    def clean(self): 

        cleaned_data = super(LoginForm, self).clean() 

        email = cleaned_data.get("email")

        password = cleaned_data.get("password") 

    # Vérifie que les deux champs sont valides
        if email and password:

            result= Person.objects.filter(email=email,password=password)
            

        
            if len(result)!=1: 

                raise forms.ValidationError("Adresse de Email ou mot de passe erroné.") 
        
        return cleaned_data 

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model=Student
        exclude=('friends','is_online')




class EmployeeProfileForm(forms.ModelForm) :
    class Meta:
        model = Employee
        exclude = ('friends','is_online')



class AddFriendForm(forms.Form) :
    email = forms.EmailField(label='Email :')
    
    def clean(self):

        cleaned_data = super(AddFriendForm,self).clean()
        email = cleaned_data.get("email")
        # Vérifie que le champ est valide
        
        if email:
            result = Person.objects.filter(email=email)
            
            
            if len(result) != 1:

                raise forms.ValidationError("Adresse de Email erronée")
            
        
        return cleaned_data
               

    


        

            
        

