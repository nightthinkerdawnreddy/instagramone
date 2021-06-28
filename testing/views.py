from django.shortcuts import render
from django.http import HttpResponse
from .models import Urlposting
import datetime

# Create your views here.
def home(request):
    return HttpResponse("<h1>hello world</h1>")
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.cleaned_data["postlink"])
            #timenow=datetime.datetime.now()
            timenow=datetime.datetime.now()
            print(timenow)
            u=Urlposting(urlpost=form.cleaned_data["postlink"],timefield=timenow,name="bhaskar")   
            u.save()
            print(u.urlpost)
            # ...
            # redirect to a new URL:
            return HttpResponse('<h1>/thanks/</h1>')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
