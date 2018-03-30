from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView,DeleteView
from django.utils import timezone
from django.urls import reverse_lazy
from blog.forms import CommentForm,PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from blog.models import Post,Comment
class AboutView(TemplateView):
    template_name='about.html'

@login_required
def post_list(request):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    args = {'object_list':queryset}
    return render(request,'blog/post_list.html',args)
@login_required
def draft_list(request):
    queryset= Post.objects.filter(published_date__isnull=True).order_by('create_date')
    args = {'object_list':queryset}
    return render(request,'blog/post_draft_list.html',args)


# class PostDetailView(DetailView):
    # model = Post
@login_required
def post_detail(request,pk=None):
    instance = get_object_or_404(Post,pk=pk)
    args={'obj':instance}
    return render(request,"blog/post_detail.html",args)
@login_required
def post_create(request):
    post_form = PostForm(request.POST)
    if request.method == "POST":

        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/blog')
        else:
            print(post_form.errors)
    else:
        post_form = PostForm()
    args={'post_form':post_form}
    return render(request,'blog/post_create.html',args)



@login_required
def post_update(request, pk=None):
    instance = get_object_or_404(Post,pk=pk)
    post_form = PostForm(request.POST,instance=instance)
    if request.method == "POST":

        if post_form.is_valid():

            post_form.save()
            return redirect('/blog')
        else:
            print(post_form.errors)
    else:
        post_form = PostForm(instance=instance)
    args={'obj':instance,'post_form':post_form}
    return render(request,"blog/post_create.html",args)

# def post_delete(request, id=None):
#     instance = get_object_or_404(Post,id=id)
#     instance.delete()
#     return refirect('/blog')

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')


@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('blog:post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail',pk=post_pk)


@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('blog:post_detail',pk=pk)
