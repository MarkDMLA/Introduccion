from django.views.generic import View
from django.shortcuts import render

# Create your views here
class BlogListViews(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'blog_list.html', context)