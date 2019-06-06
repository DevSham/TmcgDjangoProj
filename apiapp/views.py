from django.shortcuts import render, redirect
from . models import Posts
from . forms import PostsForm

# return all users.


def listAll(request):
    entries = Posts.objects.all()
    return render(request, 'apiapp/home.html', {'posts': entries})
# create user


def create(request):
    form = PostsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(listAll)  # redirect to the return method
    # this is where user goes if form is not valid
    return render(request, 'apiapp/deposit.html', {'form': form})


def update(request, id):
    entry = Posts.objects.get(id=id)
    form = PostsForm(request.POST or None, instance=entry)
    if form.is_valid():
        form.save()
        return redirect(listAll)  # redirect to the return method
    return render(request, 'apiapp/deposit.html', {'form': form, 'post': entry})


def get_absolute_url(self):
    return '/bank/get/%i/' % self.id
