from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        # creates new instance of the UserCreationForm with the form data
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()  # saves the data to the db, creating a new user
            # TBD: log user in

            return redirect('articles:list')  # redirects to /articles
    else:
        form = UserCreationForm()

    # fires after else or if form is NOT valid
    return render(request, 'accounts/signup.html', {'form': form})
