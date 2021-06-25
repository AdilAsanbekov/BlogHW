from django.contrib.auth.forms import UserCreationForm
from .forms import MyForm
from django.views.generic.edit import FormView

# Create your views here.
class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = '/users/login/'
    template_name = 'registrations/register.html'
    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)