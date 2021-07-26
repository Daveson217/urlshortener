# Python
import random
import string

# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from .models import Link

def generate_shortened_link():
    # get random string of letters and digits
    source = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(source) for i in range(7)))
    get_entry = None
    
    # Search through the database for the generated random string. If the generated random 
    # string is in the database, call the function againg (recursion)
    
    try:
        # If the shortened link exists, call the function again
        # I don't know if this is the most efficient way to do this
        get_entry = Link.objects.get(short_link=result_str)        
        generate_shortened_link()           
    except ObjectDoesNotExist:        
        return result_str   
        #generate_shortened_link()
class LinkCreateView(CreateView):
    model = Link
    template_name = "home.html"    
    fields = ['full_link']
    success_url = ''   
    
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        shortened_link = generate_shortened_link()
        form.instance.short_link = shortened_link    
        #self.success_url = reverse_lazy('return_shortened_link', args=[shortened_link])   
        self.object = form.save()     
        return redirect(reverse('return_shortened_link', kwargs={ 'short_link': shortened_link }))
        #return super().form_valid(form)

def shortened_link_redirect_view(request, short_link):
    link = Link.objects.get(short_link=short_link)
    full_url = link.full_link
    
    return redirect(full_url) 