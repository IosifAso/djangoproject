from random import random, randrange

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordContextMixin
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView

from DjangoProject.settings import EMAIL_HOST_USER
from userextend.forms import UserExtendForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserExtendForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_user = form.save(commit=False)
            new_user.is_active = False
            new_user.first_name = new_user.first_name.title()
            new_user.username = f'{new_user.first_name}{new_user.last_name.lower()}_{randrange(100000,999999)}'
            new_user.save()

            subject = 'Ti-ai creat un cont nou'
            message = f'Hello, {new_user.username} ti-ai creat cont in aplicatia mea.'
            send_mail(subject, message, EMAIL_HOST_USER, [new_user.email])

            details_user ={
                'fullname': f'{new_user.first_name} {new_user.last_name}',
                'username': f'{new_user.username}',
                'url': f'http://127.0.0.1:8000/confirm/{new_user.id}/'
            }
            subject = f'Ti-ai creat un cont nou'
            message = get_template('mail.html').render(details_user)

            mail = EmailMessage(subject, message, EMAIL_HOST_USER, [new_user.email])
            mail.content_subtype = 'html'
            mail.send()

        return redirect('login')

def confirm_account(request, pk):
    User.objects.filter(id=pk).update(is_active=True)
    return redirect('login')
