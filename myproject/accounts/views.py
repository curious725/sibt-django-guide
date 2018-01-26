from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def signup(request):
    form = UserCreationForm()
    # import pdb; pdb.set_trace()
    return render(
        request, 'accounts/signup.html', {'form': form}
    )
