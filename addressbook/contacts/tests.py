"""
 # Create your tests here.

This file demonstrates writing tests using the unittest module.
These will pass
when you will run "manage.py test".

"""
from django.test import TestCase
from contacts.models import Contact
from django.test.client import RequestFactory
from contacts.views import ContactListView

class ContactTests(TestCase):
    #Verify the correct String representation of object
    def test__str(self):
        c = Contact(first_name = 'Joey', last_name = 'Smith')
        self.assertEqual(str(c), 'Joey Smith')

# Testing ViewLogic

class ContactListViewTests(TestCase):
    
    def test_no_contacts_in_context(self):
        factory = RequestFactory()
        request = factory.get('/')
        
        response = ContactListView.as_view()(request)
        
        self.assertEquals(
            list(response.context_data['object_list']), 
            [],
        )
    
    #Contact should be present in the object_list
    def test_contacts_in_context(self):
        factory = RequestFactory()
        request = factory.get('/')
        
        c = Contact.objects.create(first_name = 'Joey', last_name = 'Smith',
                email = 'joe@example.com')
        
        response = ContactListView.as_view()(request)
        
        self.assertEquals( list(response.context_data['object_list']), [c],)
        
