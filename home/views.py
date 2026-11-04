from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import dpt
from home.models import doctor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import BookingForm,ContactInfoForm
from django.shortcuts import render
from .recommendation import recommend_doctors,find_specializations




# Create your views here.


def index(request):
    return render(request,'index.html')

@login_required
def about(request):
    # company={
    #     'name':"hosp pvt",
    #     'years':2022,

    # }

    fruites={
        'items':["orange","apple","pineapple","dragon fruit"]
    }
    return render(request,'about.html',fruites)

@login_required
def doctors(request):
    # doctor={
    #     'name':'kiran',
    #     'age':29,
    #     'years_of_experience':'5 years'
    # }
    # doctor={
    #     'names':["kiran","kumar","remesh",'kirshna']

    # }
    doctors={
        "doctors":doctor.objects.all()
    }
    return render(request,"doctors.html",doctors)

@login_required
def contact(request):
    contacts={
        'phone_no':9032123123
    }
    return render(request,"contact.html",contacts)

@login_required
def department(request):
    departments={
        'departments':dpt.objects.all()
    }
    return render(request,"department.html",departments)



@login_required
def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form=BookingForm()
            
    return render(request,"booking.html",{'form':form})


# def contact(request):
#     if request.method=="POST":
#         form=ContactInfoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("index")
#     else:
#         form=ContactInfoForm()
            
#     return render(request,"contact.html",{'form':form})


@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactInfoForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
            # Redirect to a success page
            return redirect('success')
    else:
        form = ContactInfoForm()

    return render(request, 'contact.html', {'form': form})



def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect("index")
    else:
        form=UserCreationForm()
    return render(request,"signup.html",{'form':form})
    

@login_required
def smart_recommendation(request):
    doctors = []
    symptoms = ""
    searched = False

    if request.method == "POST":
        symptoms = request.POST.get("symptoms", "").strip()
        searched = True

        if symptoms:
            doctors = recommend_doctors(symptoms)

    return render(
        request,
        "smart_recommendation.html",
        {
            "doctors": doctors,
            "symptoms": symptoms,
            "searched": searched,
        },
    )