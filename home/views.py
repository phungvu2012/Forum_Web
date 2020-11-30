from django.shortcuts import render
# ADD 
from login.models import Account
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    # Get image avatar
    account = Account.objects.get(user=request.user)
    avatar = 'media/{}'.format(account.avatar)
    # Data send font
    data = {'avatar': avatar}
    return render(request,'pages/home.html', data)
