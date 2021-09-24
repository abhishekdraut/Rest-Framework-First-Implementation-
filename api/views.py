
from rest_framework import views, response, status
from . models import blog as BlogModel
from . import serializer as Blog_serializer

# Create your views here.


class HelloAPI(views.APIView):
    serializer_class = Blog_serializer.blog
    def get(self, request):
        blogmodel = BlogModel.objects.all()
        dictionary = {}
        for key ,each_blog in enumerate(blogmodel):
            dictionary[key]={
                "title":each_blog.title,
                "details":each_blog.description,
                'date':each_blog.date,
            }

        dictionary=list(dictionary.values())
        print(dictionary)
        
        
        
        return response.Response({'data': dictionary})

    def post(self,request):

        blog_seri= self.serializer_class(data=request.data)
        if blog_seri.is_valid():
            title=blog_seri.validated_data.get('title')
            description=blog_seri.validated_data.get('description')
            date=blog_seri.validated_data.get('date')
            print(title)
            print(description)
            print(date)
            blog=BlogModel.objects.create(title=title, description=description,date=date)
            print(blog)
            blog.save()
            return response.Response({'message':'Successfully submited'}) 
        else:
            return response.Response(blog_seri.errors,status=status.HTTP_400_BAD_REQUEST)   

        
