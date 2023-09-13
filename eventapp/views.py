from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .form import Applicantform
# Create your views here.
def index(request):
    events=Event.objects.all()
    context={
        'events' :events
    }
    return render(request,'eventapp/index.html',context)

def eventdetail(request,pk):
    event_single = Event.objects.get(pk=pk)
    if request.method == 'POST':
        form = Applicantform(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.event = event_single
            applicant.save()
        #print('I got a post request from frontend')
    form=Applicantform()
    context={
        'event' : event_single,
        'form' : form
    }
    return render(request,'eventapp/event.html',context)
