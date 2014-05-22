#from django.shortcuts import render
# Create your views here.
"""
Class-Based Views`

"""
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

def index(request):
    """ Index page.
    """
    context = RequestContext(request)
    return render_to_response('contact_list.html', context)

def new_contact(request):
    """ New Contact Form.        
    """
    context = RequestContext(request)
    return render_to_response('edit_contact.html', context)
    
    def get_success_url(self):
        return reverse('contact-list')


"""
class ContactListView(ListView):
    
    model = Contact
    template_name = 'contact_list.html'
 
class CreateContactView(CreateView):
    
    model = Contact
    template_name = 'edit_contact.html' 
    
    def get_success_url(self):
        return reverse('contact-list')
"""
