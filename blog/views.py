from django.conf import settings
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts})
 
def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'manev.ru@gmail.com']
        contact_message = "%s: %s via %s"%(
            form_full_name, 
            form_message, 
            form_email)

        send_mail(subject, 
                contact_message, 
                from_email, 
                to_email, 
                fail_silently=False)

    context = {
		"form": form,
	}
    return render (request, 'forms.html', context)

 
def home(request):
    return render (request, 'home.html', {})

def blog_page(request):
    return render (request, 'blogpage.html', {})

def about(request):
    return render (request, 'about.html', {})

def first_step(request):
    return render (request, 'card_choice.html', {})

def second_step(request):
    return render (request, 'message_input.html', {})

def third_step(request):
    return render (request, 'address_input.html', {})

def final_step(request):
    return render (request, 'summary.html', {})

def sent_success(request):
    return render (request, 'postcard_sent_success.html', {})