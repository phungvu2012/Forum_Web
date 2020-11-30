from django.contrib import admin
from .models import Category, Group, GroupBelongCategory, GroupHasAccount, AccountApplyGroup, Post, AccountReportPost, Comment, accountReportComment
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']
    search_fields = ['name']
admin.site.register(Category, CategoryAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'image']
    list_filter = ['id']
    search_fields = ['name']
admin.site.register(Group, GroupAdmin)

class GroupBelongCategoryAdmin(admin.ModelAdmin):
    list_display = ['groupId', 'categoryName']
    list_filter = ['categoryName']
    search_fields = ['groupId']
admin.site.register(GroupBelongCategory, GroupBelongCategoryAdmin)

class AccountApplyGroupAdmin(admin.ModelAdmin):
    list_display = ['userName', 'groupId', 'timeApply']
    list_filter = ['groupId']
    search_fields = ['groupId']
admin.site.register(AccountApplyGroup, AccountApplyGroupAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'image', 'userName', 'groupId', 'timePost']
    list_filter = ['timePost']
    search_fields = ['content']
admin.site.register(Post, PostAdmin)

class AccountReportPostAdmin(admin.ModelAdmin):
    list_display = ['userName', 'postId', 'content', 'timeReport']
    list_filter = ['timeReport']
    search_fields = ['postId']
admin.site.register(AccountReportPost, AccountReportPostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'userId', 'postId', 'timeComment']
    list_filter = ['postId']
    search_fields = ['username']
admin.site.register(Comment, CommentAdmin)

class accountReportCommentAdmin(admin.ModelAdmin):
    list_display = ['userName', 'commentId', 'content', 'timeReport']
    list_filter = ['timeReport']
    search_fields = ['commentId']
admin.site.register(accountReportComment, accountReportCommentAdmin)

class GroupHasAccountAdmin(admin.ModelAdmin):
    list_display = ['groupId', 'userName', 'isAdmin']
    list_filter = ['groupId']
    search_fields = ['groupId']
admin.site.register(GroupHasAccount, GroupHasAccountAdmin)