from django.shortcuts import render
from login.models import Account
from django.http import HttpResponseRedirect
# ADD 
from .forms import CreateGroupForm, JoinGroupForm, CommentForm
from .models import Group, GroupHasAccount, Post, Comment
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
    commentForm = CommentForm()
    if(request.method == "POST"):
        if request.POST.get("sub") == 'Join':
            joinGroup = JoinGroupForm(request.POST, userIdPara = request.user.id, groupIdPara = id)
            if joinGroup.is_valid():
                joinGroup.save()
                return HttpResponseRedirect(request.path_info)
        if request.POST.get("sub") == 'Đăng':
            print('hello')
            commentForm = CommentForm(request.POST, userIdPara=request.user.id)
            if commentForm.is_valid():
                commentForm.save()
                return HttpResponseRedirect(request.path_info)
    try:
        checkUserInGroup = GroupHasAccount.objects.get(groupId_id=id, userName_id = request.user.id)
    except ObjectDoesNotExist:
        checkUserInGroup = False
    if checkUserInGroup:
        checkUserInGroup = True

    infPosts = []
    try:
        posts = Post.objects.filter(groupId_id = id)
    except ObjectDoesNotExist:
        posts = None
    print("Posts: ", posts)
    for post in posts:
        try:
            comments = Comment.objects.filter(postId_id = post.id)
            # print("Comments: ", comments)
        except ObjectDoesNotExist:
            comments = None
        infPosts.append({'post': post, 'comments': comments})

    return render(request, "pages/detailgroup.html", { "group": Group.objects.get(id=id), "ListPosts": infPosts, 'display': checkUserInGroup, 'joinGroup': joinGroup, "CommentForm": commentForm});
