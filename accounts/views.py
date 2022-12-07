from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        # creates new instance of the UserCreationForm with the form data
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()  # saves the data to the db, creating a new user

            login(request, user)

            return redirect('articles:list')  # redirects to /articles
    else:
        form = UserCreationForm()

    # fires after else or if form is NOT valid
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        # authenticates user, the POST data is not the expected first param so the arg is named for the function
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()

            login(request, user)

            # if the next param exists on the post request, redirect to the url attached to it
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')  # redirects to /articles

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):  # use post request because a page is not being requested, an action is
    if request.method == 'POST':
        logout(request)

        return redirect('articles:list')  # redirects to /articles/
