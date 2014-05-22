from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                                    
    url(r'^$', 'contacts.views.index',
        name = 'contact-list',
    ),
    
    url(r'^new$', 'contacts.views.new_contact',
        name = 'contacts-new',
    ),

    url(r'^admin/', 
        include(admin.site.urls)
    ),
                   
                      
    #url(r'^$', contacts.views.ContactListView.as_view(),
     #   name = 'contact-list',
    #),
        
    #url(r'^new$', contacts.views.CreateContactView.as_view(), 
     #   name = 'contacts-new',
    #),       
    # Examples:
    # url(r'^$', 'addressbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
)