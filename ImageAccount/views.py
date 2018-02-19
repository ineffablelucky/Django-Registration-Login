from django.shortcuts import render, redirect, HttpResponse
from ImageAccount.forms import RegisterationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def useraccount(request):
    return render(request, 'ImageAccount/index.html')


def contact_page(request):
    return render(request, 'ImageAccount/contact.html')


def register(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        try:
            if form.is_valid:
                form.save()
                return HttpResponse("""<p>Registration Done!!</p>\
                <p><a href="/useraccount/"><button type="button">Home</button></a>\
                </p>""")
                #return redirect('useraccount')
        except ValueError:  # have to test it out
            return HttpResponse("\
            <h1>Go Back, Read The Instructions and Then Enter Data Carefully.\
            Also, You must have a unique username.</h1>")
    else:

        form = RegisterationForm()
        context = {'form': form}
        return render(request, 'ImageAccount/register_form.html', context)

@login_required
def view_profile(request):
    context = {'user' : request.user}
    return render(request, 'ImageAccount/profile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('view_profile')

    else:
        form = EditProfileForm(instance = request.user)
        context = {'form': form}
        return render(request, 'ImageAccount/edit_profile.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('view_profile')

        else:
            return redirect ('change_password')
    else:
        form = PasswordChangeForm(user = request.user)
        context = {'form': form}
        return render(request, 'ImageAccount/change_password.html', context)
