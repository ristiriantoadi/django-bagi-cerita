from django.contrib.auth.forms import UserCreationForm

def get_auth_form(request):
    registerForm = UserCreationForm()
    return{
        'register_form':registerForm
    }
