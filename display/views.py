from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # Note, in the future, this should display [X].html
    # depending on what sort of display i want to render
    # hm on second thought, no there should just be another
    # function definition shouldn't there?
    # I guess the index here should ask what graph you want
    # to display.
    return render(request, 'display/display_home.html')

