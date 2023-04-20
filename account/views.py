from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from .forms import RegisterForm, InstagramForm
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from .tools.login_helper import AuthView, IsNotAuthView
from .models import Instagram
from django.shortcuts import get_object_or_404

class SignUpView(AuthView,CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        to_return = super().form_valid(form)
        login(self.request, self.object)
        return to_return

class SignInView(AuthView,LoginView):
    template_name = 'login.html'

    def get_success_url(self) -> str:
        return reverse_lazy("home")
    
class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'

class AddInstagramView(CreateView):
    form_class = InstagramForm
    template_name = 'add_instagram.html'

    def form_valid(self, form):
        obj = form.save(commit = False)
        obj.user = self.request.user
        obj.save()
        return redirect(reverse_lazy("home"))
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy("home"))
        try:
            if hasattr(request.user.instagram):
                return redirect(reverse_lazy("home"))
        except:
            return super().dispatch(request, *args, **kwargs)
    
class UpdateInstagramView(UpdateView):
    form_class = InstagramForm
    template_name = 'add_instagram.html'
    model = Instagram

    def form_valid(self, form):
        obj = form.save(commit = False)
        obj.user = self.request.user
        obj.save()
        return redirect(reverse_lazy("home"))
    
    def get_object(self):
        return get_object_or_404(Instagram, user=self.request.user)


def logout_view(request):
    logout(request)
    return redirect('login')
    