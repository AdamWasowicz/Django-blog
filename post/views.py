from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request):
        dummy_posts = [
            {
                'title': 'title1',
                'content': "content1"
            },
            
            {
                'title': 'title2',
                'content': "content2"
            }
        ]
        return render(request, './post/index.html', {
            'posts': dummy_posts
        })


