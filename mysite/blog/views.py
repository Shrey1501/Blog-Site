from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.forms import PostForm,CommentForm
from blog.models import Post,Comment
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,
                                        CreateView,UpdateView,DeleteView)


# Create your views here.

# 1. For ABOUT ME PAGE
class AboutView(TemplateView):
    template_name = 'about.html'

# 2. List all the approved posts here. This is also our Landing Page
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # lte - less than or equal to

# 3. To view the details of the post such as its content, comments.
class PostDetailView(DetailView):
    model = Post

# 4.  To create a new post
class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model=Post

# 5. To edit or delete the published posts by the superuser
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model=Post

# 6. To delete a post by the superuser
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

# 6. After a post is created it is saved into drafts so that it can be approved or disapproved by the superuser.
class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')

##############################################################
####################################################
# 7. To publish a post
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('blog:post_detail',pk=pk)

# 8. To add comment to a post
@login_required
def add_comment_to_post(request,pk):
    post  = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail',pk=pk)

    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment  = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('blog:post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail',pk=post_pk)
