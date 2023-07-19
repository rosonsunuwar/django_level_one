from django.shortcuts import render
# from django.http import HttpResponse
# from second_app.models import Users
from second_app.forms import NewUserForm
# Create your views here.
def index(request):
    return render(request, 'second_app/index.html')
    

def user(request):
    
    form = NewUserForm
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, 'second_app/user.html', {'form' : form})