from django.shortcuts import render
from login.models import Account
from django.http import HttpResponseRedirect
# ADD 
from .forms import CreateGroupForm, JoinGroupForm
from .models import Group, GroupHasAccount, Post
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def listgroup(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    # Get image avatar
    account = Account.objects.get(user=request.user)
    avatar = 'media/{}'.format(account.avatar)
    # Data send font
    name = request.user.first_name + request.user.last_name
    # Tạo form
    form = CreateGroupForm()
    if request.method == 'POST':
        form = CreateGroupForm(request.POST, request.FILES, userIdPara = request.user.id)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
    data = {'avatar': avatar, 'name': name, 'form': form, 'Groups': Group.objects.all()}
    # response request
    return render(request, 'pages/listgroup.html', data)

def detailGroup(request, id):
    joinGroup = JoinGroupForm()
    if(request.method == "POST"):
        joinGroup = JoinGroupForm(request.POST, userIdPara = request.user.id, groupIdPara = id)
        if joinGroup.is_valid():
            joinGroup.save()
            return HttpResponseRedirect(request.path_info)
    try:
        checkUserInGroup = GroupHasAccount.objects.get(groupId_id=id, userName_id = request.user.id)
    except ObjectDoesNotExist:
        checkUserInGroup = False
    if checkUserInGroup:
        checkUserInGroup = True
    posts = Post.objects.filter(groupId_id = id);
    return render(request, "pages/detailgroup.html", { "group": Group.objects.get(id=id), "Posts": posts, 'display': checkUserInGroup, 'joinGroup': joinGroup});