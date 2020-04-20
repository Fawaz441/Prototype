from .forms import OfferForm,PostForm
from .models import Offer,Post
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    if request.method=='POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('client_name')
            service = form.cleaned_data.get('service')
            email = form.cleaned_data.get('email')
            number = form.cleaned_data.get('number')

            offer = Offer.objects.create(
                client_name=name,
                service = service,
                email=email,
                number=number,
                created_at = timezone.now()
            )
            offer.save()
            messages.info(request,'Form submitted successfully!')
            return redirect('home')
        else:  
            messages.warning(request,'Form is not valid! Please try again.')
            return render(request,'index.html',{'form':form})

    else:
        form = OfferForm()
    return render(request,'index.html',{'form':form})


class PostCreate(generic.View):
    def get(self,*args,**kwargs):
        form = PostForm()
        return render(self.request,'post_create.html',{'form':form})

    def post(self,*args, **kwargs):
        if self.request.method == "POST":
            form = PostForm(self.request.POST,self.request.FILES)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')
                image = form.cleaned_data.get('image')
                area = form.cleaned_data.get('area').replace("[","").replace("]","")
                area = area.replace("\'","")
                print(form.cleaned_data)
                post = Post.objects.create(
                    title = title,
                    content = content,
                    image = image,
                    area = area,
                    author = self.request.user,
                )
                post.save()
                return redirect('detail',slug=post.slug)
            else:
                messages(self.request,'Your form has issues')
                return redirect('post_create')
        
class Draftview(generic.ListView):
    model = Post
    template_name = 'drafts.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_at').all()
        

class PublishedPosts(generic.ListView):
    model = Post
    template_name = 'posts.html'

    
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=False).order_by('-published_date').all()


class PostDetail(generic.DetailView):
    model = Post    
    template_name = 'post_detail.html'

class PostDelete(LoginRequiredMixin,generic.DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
    template_name = 'post_delete.html'

    def delete(self,*args, **kwargs):
        messages.info(self.request,'Deleted Successfully')
        return super().delete(self.request,*args, **kwargs)

def publish(request,slug):
    post = get_object_or_404(Post,slug=slug)
    if request.user.is_superuser:
        post.publish()
        messages.info(request,'Published successfully')
        return redirect('detail',slug=slug)
    else:
        messages.warning(request,'You are not authorized to carry out this action')
        return redirect('home')
        

class DesignsView(generic.TemplateView):
    template_name = 'designs.html'