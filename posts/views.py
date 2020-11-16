from django.shortcuts import render, redirect


# POSTS VIEW ENDPOINT
def posts(request):
    if request.user.is_authenticated:
        return render(request, 'blog-listing.html')
    return redirect('login')


# POST DETAILS VIEW ENDPOINT
def post_details(request):
    return render(request, 'blog-post.html')
