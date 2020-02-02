from django.shortcuts import render
from .models import Users
from django.http import Http404, JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import random, serial, time

# Create your views here.
ser = serial.Serial('COM8', baudrate=115200, timeout=1)
time.sleep(2)
def realTimeData(request):
    if request.is_ajax():
        aurdinoData = ser.readline().decode('ascii').split('|')
        
        print(aurdinoData)
        if len(aurdinoData)==8:
            muserdata = {
                'threshold' : aurdinoData[0],
                'temperature': aurdinoData[1],
                'humidity' : aurdinoData[2],
                'light' : 'off' if aurdinoData[3]=='0' else 'on',
                'food' : 'normal' if aurdinoData[4]=='0' else 'low  ',
                'fan' : 'off' if aurdinoData[5]=='0' else 'on',
                'heater' : 'off' if aurdinoData[6]=='0' else 'on'
                }
        return JsonResponse(muserdata)
    return render(request, 'app/user.html')



def input(request):
    if request.is_ajax():
        val=str(request.GET.get('val')+'\n')
        print(val)
        ser.write(str.encode(val))
        return JsonResponse({})

def index(request):
    return HttpResponse("<h1>Monitoring System</h1>")