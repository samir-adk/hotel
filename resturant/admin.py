from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from resturant.models import BlogComment,Customer,Book,Room,Staff,Blog,AboutUs
# Register your models here.






admin.site.site_header="HOTEL MILLENNIUM BLUE"
admin.site.site_title="HOTEL MILLENNIUM BLUE"
admin.site.index_title = "HOTEL MILLENNIUM BLUE"

class CustomerAdmin(admin.ModelAdmin):
    list_display=('name','phone','email','message','registered_at')
    search_fields=['name','phone']
    date_hierarchy = 'registered_at'

class BookAdmin(admin.ModelAdmin):
  list_display=('room','no_guests','arrival_date','departure_time','phone','message','created_at')
  search_fields=['room','arrival_date','no_guests','phone']

class AboutUsAdmin(admin.ModelAdmin):
    list_display=('company_name','company_motto','about_us','description','address','phone','email','images','about_page_image','created_at')
    formfield_overrides = {
    models.TextField: {'widget': Textarea(attrs={'rows':20, 'cols':20})},
    }
class BlogAdmin(admin.ModelAdmin):
    list_display=('category','title','about','image','created_at')
    search_fields=['category','title']
    date_hierarchy='created_at'
    formfield_overrides = {
    models.TextField: {'widget': Textarea(attrs={'rows':20, 'cols':20})},
    }



class StaffAdmin(admin.ModelAdmin):
    list_display=('depart','name','image','about','created_at')
    search_fields=['name','depart']
    date_hierarchy='created_at'

class RoomAdmin(admin.ModelAdmin):
    list_display=('feature_name','room_number','image','people','area','details','price','Featured_image','normal_display','created_at')
    search_fields=['feature_name','room_number']
    date_hierarchy='created_at'

class BlogCommentAdmin(admin.ModelAdmin):
    model = BlogComment
    list_display=['get_blog','comment','profile','commenter','comment_date']
    search_fields=['commenter']
    date_hierarchy='comment_date'

    def get_blog(self,obj):
        return obj.main_blog.category




admin.site.register(Customer,CustomerAdmin)
admin.site.register(AboutUs,AboutUsAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Staff,StaffAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(BlogComment,BlogCommentAdmin)
admin.site.register(Book,BookAdmin)