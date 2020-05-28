from django.shortcuts import render
from django.views import View

from .forms import PostForm
from .models import Post

class IndexView(View):
    model = Post
    form_class = PostForm
    template_name = "app/index.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        posts = self.model.objects.all().order_by('-id')[:20]
        return render(request, self.template_name, {'form': form, 'posts': posts})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        posts = self.model.objects.all().order_by('-id')[:20]
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {'form': form, 'posts': posts})

        return render(request, self.template_name, {'form': form, 'posts': posts})