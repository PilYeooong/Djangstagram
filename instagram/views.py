from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.tag_set.add(*post.extract_tag_list()) # 다대다 관계에서는 pk가 요구되기때문에 save() 호출 뒤에 실행
            messages.success(request, '포스팅을 생성하였습니다.')
            return redirect('/')  # get_absolute_url
    else:
        form = PostForm()

    return render(request, 'instagram/post_form.html', {
        'form': form,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'instagram/post_detail.html', {
        'post': post
    })