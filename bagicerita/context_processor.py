from django.contrib.auth.forms import UserCreationForm

def get_auth_form(request):
    registerForm = UserCreationForm()
    return{
        'register_form':registerForm
    }

def check_if_logged_in(request):
    if request.user.is_authenticated:
        # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        return{
            'logged_in':True,
            'username':request.user.username
        }
    else:
        return {
            'logged_in':False
        }