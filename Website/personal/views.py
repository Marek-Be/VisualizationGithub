from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import getUser
from .forms import UsernameForm

def index(request):
    if request.method == 'POST':
        username = request.POST.get("your_name")
        things = getUser.getRepoData(username)
        print(things)
        if (things == None):
            return render(request, 'personal/home.html', {'Error': 'An error occured, this is probably because too many requests were given to the github api. Check server for details'})
        return render(request, 'personal/home.html', {'categories': things[0], 'colors': things[1], 'data': things[2]})
    return render(request, 'personal/home.html',)


def contact(request):
    return render(request, "personal/basic.html", {'content':['If you would like to contact me, please email me at "whatever"','']})
