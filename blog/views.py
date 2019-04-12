from django.shortcuts import render

def posts_list(request):
    n = ['Tom', 'Jack', 'Tim']
    return render(request, 'blog/index.html', context={'names': n})
