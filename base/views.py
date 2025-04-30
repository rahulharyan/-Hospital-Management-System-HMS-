from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from base.models import AddPatient

# Create your views here.

@login_required(login_url='login_')
def home(request):
    context={}
    import requests
    api_key='4be5c277cc93562237fdffef3c8e8218'

    weather_api='https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'
    weather_data=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=bangalore&appid={api_key}')

    if weather_data.status_code == 200:
        weather_data == weather_data.json()
        print(weather_data)
        context['whether_data']=weather_data
    else:
        context['error'] = 'could not fetch whether data'

    context[weather_data]=weather_data
    return render(request, 'home.html',context)

def add_patient(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        address=request.POST['address']
        email=request.POST['email']
        phone=request.POST['phone']
        AddPatient.objects.create(first_name=firstname,last_name=lastname,address=address,email=email,phone=phone)
        return redirect('list')
    return render(request ,'add_patient.html')

@login_required(login_url='login_')
def list(request):
    all_patient_data=AddPatient.objects.all()
    return render(request ,'list.html',{'all_patient_data':all_patient_data})


def remove(request,pk):
    patient=AddPatient.objects.get(id=pk)
    patient.delete()
    return redirect('list')