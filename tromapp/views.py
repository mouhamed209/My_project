from tromapp.forms import LoginForm
from django.shortcuts import render,redirect
from tromapp.forms import  StudentProfileForm,EmployeeProfileForm,AddFriendForm
from django.http import HttpResponse
from tromapp.models import Person,Student,Employee,Message,Invitation
from datetime import date
from django import forms
from django.http import JsonResponse
from django.db.models import Q

def login(request):
        if 'logged_user_id'in request.session:
           
            if request.session['logged_user_id']!='':
                return redirect('/')
        if len(request.POST)>0:
            form = LoginForm(request.POST)
            if form.is_valid():
                user_email= form.cleaned_data['email']
                logged_user= Person.objects.get(email=user_email)
                request.session['logged_user_id'] =logged_user.id
                return redirect('/welcome')
            else:
                return render(request,'login.html',{'form':form})
        else:
            form= LoginForm()
            return render(request,'login.html',{'form':form})
def welcome(request):
    try:
    
        logged_user = get_logged_user_form_request(request)
        if logged_user:
            logged_user.is_online=True
            logged_user.save()
            
            if 'newMessage' in request.GET and request.GET['newMessage']!='':
            
                newMessage = Message(author=logged_user,content=request.GET['newMessage'],publication_date = date.today())
                    
                newMessage.save()
                # request.GET["newMessage"]=''
                    
            if 'userOut' in request.GET and request.GET['userOut']=='out':
                logged_user.is_online=False
                logged_user.save()
                request.session["logged_user_id"]=''

                return redirect('/login')

                
                
                
            if 'Dfriend' in request.GET and request.GET['Dfriend']!='':
                x = int(request.GET['Dfriend'])
                logged_user.friends.remove(x)
            return render(request, 'welcome.html',{'logged_user': logged_user})

            

        else:
            return redirect('/login')
    except :
        return redirect('/login')
from django.db.models import Q
def update_messages(request):
    logged_user = get_logged_user_form_request(request)
    friendMessages = Message.objects.filter(Q(author__friends=logged_user)|Q(author=logged_user)).order_by('publication_date', 'publication_time').reverse().distinct()
    htmlM = '<ul id="friendMessageList"> '
    for message in friendMessages:
        htmlM += '<li>'
        htmlM += '<p>'
        htmlM += '<a href="showProfile?userToShow=' + str(message.author.id) + '"'+'>'
        htmlM +=  message.author.first_name + ' ' + message.author.last_name + '</a> dit :'
        htmlM += '</p>'
        htmlM += '<p>' + message.content + '</p>'
        htmlM += '</li>'
    htmlM += '</ul>'
    return HttpResponse(htmlM)
def get_logged_user_form_request(request):
    if 'logged_user_id' in request.session:
        logged_user_id= request.session['logged_user_id']
        if len(Student.objects.filter(id=logged_user_id))==1:
            return  Student.objects.get(id=logged_user_id)
        elif  len(Employee.objects.filter(id=logged_user_id))==1:
            return Employee.objects.get(id=logged_user_id)
        else: 
            return None
    else:
        return None

def add_friend(request):
    try:
        logged_user=get_logged_user_form_request(request)
        if logged_user:
            if len(request.GET)>0:
                form=AddFriendForm(request.GET)
                if form.is_valid():
                    new_friend_email=form.cleaned_data["email"]
                    new_friend= Person.objects.get(email=new_friend_email)
                    if logged_user.email==new_friend_email:
                        return render(request,'add_friend.html',{'form':form, 'erreur':"Vous ne pouvez pas vous rajouter"})
                    
                    
                    
                    if Invitation.objects.filter(sender=new_friend,recipient=logged_user).exists():
                        return render(request,'add_friend.html',{'form':form,'erreur':"cette personne t'a deja envoyeé une invitation"})

                   
                    
                    if Invitation.objects.filter(sender=logged_user, recipient=new_friend).exists():
                        return render(request,'add_friend.html',{'form':form,'erreur':'envoie deja'})
                    elif logged_user.friends.filter(email=new_friend_email).exists():
                        return render(request,'add_friend.html',{'form':form,'erreur':'Cette personne est deja votre amis'})
                    else:
                        invitation = Invitation(sender=logged_user, recipient=new_friend)
                        invitation.save()

                    
                    return redirect('/welcome')
                else:
                    return render(request,'add_friend.html',{'form':form})
            else:
                form= AddFriendForm()
                return render(request,'add_friend.html',{'form':form})
        else:
            return redirect('/login')
    except:
        return redirect('/login')

 #pour voir le profile
            #    
def show_profile(request):
    try:
        logged_user = get_logged_user_form_request(request)
        

        if logged_user:
                    # Teste si le paramétre attendu est bien passé
            
            if 'userToShow' in request.GET and request.GET['userToShow'] != '': 
                user_to_show_id = int(request.GET['userToShow']) 
                results = Person.objects.filter(id=user_to_show_id) 
                if len(results) == 1:
                    if Student.objects.filter(id=user_to_show_id):
                        user_to_show = Student.objects.get(id=user_to_show_id) 

                                

                                
                    else:
                        user_to_show = Employee.objects.get(id=user_to_show_id) 
                    return render(request, 'show_profile.html',{'user_to_show': user_to_show}) 
                        
                else:
                    return render(request, 'show_profile.html',{'user_to_show': logged_user}) 
                    
                    # Le paramétre n'a pas été trouvé
            else:
                return render(request, 'show_profile.html',{'user_to_show': logged_user})
                
        else:
            return redirect('/login')
    except:
        return redirect('/login')  
def modify_profile(request):
        try:    
            logged_user =get_logged_user_form_request(request)       
            if logged_user:
                if len(request.GET) > 0:
                    a= logged_user.email
                    if type(logged_user) == Student:
                        form= StudentProfileForm(request.GET, instance=logged_user)
                        email=request.GET['email']
                    else:
                        form=EmployeeProfileForm(request.GET,instance=logged_user)
                        email=request.GET['email']
                                                                
                    if form.is_valid():
                            if Person.objects.filter(email=email).exists()==True and email!=a:
                                if type(logged_user)==Student:
                                    form=StudentProfileForm(request.GET,instance=logged_user)
                                else:
                                    form=EmployeeProfileForm(request.GET,instance=logged_user)
                                return render(request,'modify_profile.html',{'form':form ,'er':True})
                            else:
                                form.save()
                                return redirect('/')
                                
                        
                                
                    else:
                        return render(request,'modify_profile.html',{'form':form, 'er':False})
                            
                        
                else:
                    
                    if type(logged_user) == Student:
                            form = StudentProfileForm(instance=logged_user)
                    else:
                            form = EmployeeProfileForm(instance=logged_user)

                    return render(request, 'modify_profile.html',{'form':form,'er':False})
            else:
                return redirect('/login')
        except:
            return redirect('/login')
# register
def register(request):
    if request.session['logged_user_id']=='':
        erreur=False
    
        if len(request.POST)>0 and 'profileType'in request.POST:
        
            studentForm= StudentProfileForm(prefix='st')
            employeeForm= EmployeeProfileForm(prefix='em')
            
            if request.POST['profileType']== 'student':
                studentForm = StudentProfileForm(request.POST,prefix='st')
                email= request.POST['st-email']
                if studentForm.is_valid():

                    if Student.objects.filter(email=email).exists()==True:


                        erreur=True
                    
                        return render(request,'user_profile.html',{'studentForm':studentForm,'employeeForm':employeeForm, 'er':erreur})
                    elif Student.objects.filter(email=email).exists()==False:
                        erreur=False
                        studentForm.save()
                        logged_user=Person.objects.get(email=email)
                        request.session['logged_user_id']=logged_user.id


                        return redirect('/')  
                
            elif request.POST['profileType']=='employee':
                employeeForm = EmployeeProfileForm(request.POST, prefix='em')
                email= request.POST['em-email']
                
                if employeeForm.is_valid():
                    if Employee.objects.filter(email=email).exists()==True:
                        erreur=True
                        return render(request,'user_profile.html',{'studentForm':studentForm,'employeeForm':employeeForm, 'er':erreur})
                    elif Employee.objects.filter(email=email).exists()==False:
                        employeeForm.save()
                        request.session['logged_user_id']=logged_user.id

                        return redirect('/')
            return render(request,'user_profile.html',{'studentForm':studentForm,'employeeForm':employeeForm,'er':erreur})
                                                        
        else:
            erreur=False
            studentForm=StudentProfileForm(prefix='st')
            employeeForm=EmployeeProfileForm(prefix='em')
            return render(request,'user_profile.html',{'studentForm':studentForm,'employeeForm':employeeForm, 'er':erreur})  
    else:
        return redirect('/welcome')    
def invitation(request):

    try:
        logged_user= get_logged_user_form_request(request)
        if logged_user:
            invitations = Invitation.objects.filter(recipient=logged_user)
            if 'Accepter' in request.GET and request.GET['Accepter']!='':
                x=int(request.GET['Accepter'])
                newfriend= Person.objects.get(id=x)
                logged_user.friends.add(newfriend)
                inv=Invitation.objects.filter(recipient=logged_user,sender=x)
                inv.delete()
                return redirect('/')
            if 'Refuser' in request.GET and request.GET['Refuser']!='':
                y= int(request.GET['Refuser'])
                inv=Invitation.objects.filter(recipient=logged_user,sender=y)
                inv.delete()
                return redirect('/')
                
        
        
            return render(request,'inv.html',{'invitations': invitations})
        else:
            return redirect("/login")
    except:
        return redirect('/login')
def leninv(request):
    logged_user=get_logged_user_form_request(request)
    inv = Invitation.objects.filter(recipient=logged_user) 
    if inv==None:
        invi='0'   
    else:
        invi= str(inv.count()) 
    return HttpResponse(invi)    
def friend_online(request):     
        logged_user=get_logged_user_form_request(request)
        html_friend='<ul class="lis">'
        list_friend = logged_user.friends.all()
        for friend in list_friend.all():
            html_friend+='<li>'
            html_friend+='<a href="showProfile?userToShow='+str(friend.id )+'"'+'>'
            html_friend+= friend.first_name+' '+friend.last_name+'</a>'
            if friend.is_online:
                html_friend+='<span style="color:#3b5998;margin: 0px 3px; font-size: 13px;">online</span>'
            html_friend+= '<a href="?Dfriend='+str(friend.id)+'"'+"style='text-decoration: none; color:brown; margin-left:5px;'>X</a>"
            html_friend+='</li>'
        html_friend+='</ul>'      
        return HttpResponse(html_friend)
def not_online(request):
    logged_user=get_logged_user_form_request(request)
    if logged_user:
        logged_user.is_online=False
        logged_user.save()   
        return HttpResponse("online")

        








    
        
            
      
               
            
                 


       
          

       
      
       
 
        
   


    

          

       
      
       
 
        
   


    
          

       
      
       
 
        
   


    



# ننننننننن