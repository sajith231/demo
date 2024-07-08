from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomLoginForm
from django.contrib.auth import login,authenticate,logout
from .models import Application,User
from .models import Job
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.contrib import messages
# from .forms import JobForm


def index(request):
    return render(request, 'jobapp/index.html')


def about(request):
    return render(request, 'jobapp/about.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            user = form.save()
            # Create UserProfile
            UserProfile.objects.create(
                user=user,
                phone_number=form.cleaned_data.get('phone_number'),
                qualification=form.cleaned_data.get('qualification'),
                experience=form.cleaned_data.get('experience'),
                skills=form.cleaned_data.get('skills'),
                resume=form.cleaned_data.get('resume'),
            )
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'jobapp/signup.html', {'form': form})

def login_form(request):
        if request.method == 'POST':
            
            form=CustomLoginForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                request.session['username']=username
                if user is not None:
                    request.session['id']=user.id
                    login(request, user)
                    return redirect(index)
                else:
                    return render(request,'jobapp/login.html',{'form':form})
            else:
                    return render(request,'jobapp/login.html',{'form':form})
        else:
            form=CustomLoginForm()
            return render(request,'jobapp/login.html',{'form':form})
        

        
def signout(request):
    if 'username' in request.session:
        del request.session['username']
        logout(request)
        return redirect('login')
    


@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()

            
            user_profile.phone_number = form.cleaned_data['phone_number']
            user_profile.qualification = form.cleaned_data['qualification']
            user_profile.experience = form.cleaned_data['experience']
            user_profile.skills = form.cleaned_data['skills']
            if 'resume' in request.FILES:
                user_profile.resume = request.FILES['resume']
            user_profile.save()

            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('edit_profile')  
    else:
        form = ProfileUpdateForm(instance=request.user, initial={
            'phone_number': user_profile.phone_number,
            'qualification': user_profile.qualification,
            'experience': user_profile.experience,
            'skills': user_profile.skills,
            
        })

    return render(request, 'jobapp/edit_profile.html', {'form': form})


@login_required 
def apply_for_job(request, job_id):
    job = Job.objects.get(id=job_id)
    candidate = request.user 
    application = Application.objects.create(job=job, candidate=candidate)
    return redirect('success')



def success(request):
    return render(request, 'jobapp/success.html')

def job(request):
    data_value = Job.objects.all().order_by('-id')
    for data in data_value:
        data.first_sentence = data.description.split('.')[0] + '.' if '.' in data.description else data.description

    return render(request, 'jobapp/job.html', {'datas': data_value})
    


def readmore(request, id):
    job = get_object_or_404(Job, id=id)
    return render(request, 'jobapp/readmore.html', {'job': job})




