from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from .models import Profile
# from .forms import Profile_Model_Form

class profile_Create(CreateView):
    model = Profile
    # form_class = Profile_Model_Form
    fields = '__all__'
    template_name = 'posts/profile.html'  # Your HTML template

    # def form_valid(self, form):
    #     # Optionally, do something with the uploaded image before saving
    #     # For example, you can access the form data using form.cleaned_data['image']
    #     return super().form_valid(form)