from django import forms
from .models import Category, Group, GroupHasAccount, GroupBelongCategory, AccountApplyGroup, Comment
class CreateGroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.authorId = kwargs.pop('userIdPara', None)
        super().__init__(*args, **kwargs)
    class Meta:
        model = Group
        fields = ['name', 'description', 'image'] 
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    def save(self):
        new_group = Group.objects.create(name=self.cleaned_data['name'], description=self.cleaned_data['description'], image = self.cleaned_data['image'])
        GroupBelongCategory.objects.create(categoryName=self.cleaned_data['category'], groupId_id=new_group.id)
        GroupHasAccount.objects.create(groupId_id=new_group.id, userName_id = self.authorId, isAdmin=True)
        AccountApplyGroup.objects.create(groupId_id = new_group.id, userName_id = self.authorId)

class JoinGroupForm(forms.Form):
    reasonJoinGroup = forms.CharField(widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        self.authorId = kwargs.pop('userIdPara', None)
        self.groupId = kwargs.pop('groupIdPara', None)
        super().__init__(*args, **kwargs)
    def save(self):
        AccountApplyGroup.objects.create(groupId_id=self.groupId, userName_id=self.authorId)

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.authorId = kwargs.pop('userIdPara', None)
        super().__init__(*args, **kwargs)
    postId = forms.IntegerField()
    class Meta: 
        model = Comment
        fields = ["content"]
    def save(self):
        print('save')
        Comment.objects.create(content=self.cleaned_data["content"], postId_id=self.cleaned_data["postId"], userId_id=self.authorId)