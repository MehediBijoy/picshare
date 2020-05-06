from django.shortcuts import get_object_or_404, HttpResponseRedirect, render, redirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from .models import *
from .forms import AddComment


def HomeView(request):
    context = {'images': Images.objects.all()}
    return render(request, 'Home.html', context)


class ImageDetailsView(DetailView):
    template_name = 'ImageDetails.html'
    model = Images

    def get_context_data(self, **kwargs):
        context = super(ImageDetailsView, self).get_context_data(**kwargs)
        image = get_object_or_404(Images, pk=self.kwargs.get('pk'))
        context['form'] = AddComment()
        context['comments'] = Comment.objects.filter(image=image)
        if image.likes.filter(id=self.request.user.id).exists():
            context['is_liked'] = True
        else:
            context['is_liked'] = False
        return context


class ImageUploadView(CreateView):
    template_name = 'ImageUpload.html'
    model = Images
    fields = ['title', 'image', 'details']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def Image_likes(request):
    image = get_object_or_404(Images, id=request.POST.get('image_id'))
    if image.likes.filter(id=request.user.id).exists():
        image.likes.remove(request.user)
    else:
        image.likes.add(request.user)
    return HttpResponseRedirect(image.get_absolute_url())


def Image_delete(request):
    Images.objects.filter(id=request.POST.get('image_id')).delete()
    return redirect('home_view')


def Image_comment(request):
    image = get_object_or_404(Images, id=request.POST.get('image_id'))
    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.image = image
            form.save()
    return HttpResponseRedirect(image.get_absolute_url())
