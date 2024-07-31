from django.contrib import admin
from home.models import User,Message

# Register your models here.

class UserInfo(admin.ModelAdmin):
    list_display=['userName','ageBracket']
admin.site.register(User,UserInfo)


class MessagesInfo(admin.ModelAdmin):
    list_display=['senderName','receiverName','ageBracket','message']
admin.site.register(Message,MessagesInfo)

