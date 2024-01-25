from django.shortcuts import render
from resturant.models import Staff,Customer,Room,Blog,AboutUs,BlogComment
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from resturant.forms import BookForm,FrontBook

# Create your views here.
def dashboard(request):
    get_featured_room=Room.objects.filter(Featured_image=True)[:1]
    get_display_room=Room.objects.filter(normal_display=True)[:2]
    blog_details=Blog.objects.all().order_by('-created_at')[:3]
    about_us=AboutUs.objects.all()
    return render(request,'index.html',{'about_us':about_us,'blog_details':blog_details,'featured':get_featured_room,'get_display_room':get_display_room})

def book_now(request):
    form=BookForm()
    get_dataz=Room.objects.all()[:1]
    about_us=AboutUs.objects.all()
    if request.method=='POST':
        save_data=BookForm(request.POST,None)
        if save_data.is_valid():
            save_data.save()
            messages.success(request, 'Successfully Booked.')
            return HttpResponseRedirect(reverse('resturant:book_now'))
        messages.add_message(request, 'something Went Wrong.')
        return HttpResponseRedirect(reverse('resturant:book_now'))
    return render(request,'booknow.html',{'get_dataz':get_dataz,'form':form,'about_us':about_us})

def contact(request):
    about_us=AboutUs.objects.all()
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('phone'):
            save_data=Customer()
            save_data.name=request.POST.get('name')
            save_data.phone=request.POST.get('phone')
            save_data.email=request.POST.get('email')
            save_data.message=request.POST.get('message')
            save_data.save()
            messages.success(request, 'Thanks for contacting us')
            return HttpResponseRedirect(reverse('resturant:contact'))
        else:
            messages.success(request, 'something Went Wrong')
            return HttpResponseRedirect(reverse('resturant:contact'))

    return render(request,'contact.html',{'about_us':about_us})

def book_front(request,id):
    about_us=AboutUs.objects.all()
    get_data=Room.objects.filter(id=id)
    new_id=id+1
    get_dataz=Room.objects.filter(id=new_id)
    if get_dataz:
        print('available')
    get_dataz=Room.objects.filter(id=id)
    form=FrontBook()
    if request.method=='POST':
        save_data=FrontBook(request.POST,None)
        if save_data.is_valid():
            fs=save_data.save(commit=False)
            fs.room_id=id
            fs.save()
            messages.success(request,'Successfully booked')
            return HttpResponseRedirect(reverse('resturant:book_now'))
        messages.success(request,'Something went Wrong')

        return HttpResponseRedirect(reverse('resturant:booknow'))

    return render(request,'booknow.html',{'about_us':about_us,'get_dataz':get_dataz,'form':form,'get_data':get_data})


def blog_page(request):
    all_blog=Blog.objects.all()
    about_us=AboutUs.objects.all()
    return render(request,'blog.html',{'all_blog':all_blog,'about_us':about_us})


def single_blog(request,id):
    about_us=AboutUs.objects.all()
    get_blog=Blog.objects.get(id=id)
    get_limited_blog=Blog.objects.all()[:3]
    get_comment=BlogComment.objects.filter(main_blog__id=id)
    get_comment_count=BlogComment.objects.filter(main_blog__id=id).count()
    get_categories=Blog.objects.values('category','id')
    print(get_categories)
    
    return render(request,'blog-single.html',{'get_categories':get_categories,'get_limited_blog':get_limited_blog,'get_comment_count':get_comment_count,'get_comment':get_comment,'get_blog':get_blog,'about_us':about_us})


def about_us(request):
    about_us=AboutUs.objects.all()
    staff_details=Staff.objects.all()[:3]
    return render(request,'about.html',{'staff_details':staff_details,'about_us':about_us})

def room_filter(request,id):
    if id==1:
        about_us=AboutUs.objects.all()
        get_data=Room.objects.filter(room_quality='presidential')
        return render(request,'rooms.html',{'get_data':get_data,'about_us':about_us})
    elif id==2:
        about_us=AboutUs.objects.all()
        get_data=Room.objects.filter(room_quality='luxury')
        return render(request,'rooms.html',{'get_data':get_data,'about_us':about_us})
    
    else:
        about_us=AboutUs.objects.all()
        get_data=Room.objects.filter(room_quality='deluxe')
        return render(request,'rooms.html',{'get_data':get_data,'about_us':about_us})


    return render(request,'rooms.html',{'about_us':about_us})