from django.shortcuts import render


def post_list(request):
    tpl = 'blog/post_list.html'
    ctx = {}
    return render(request, tpl, ctx)
