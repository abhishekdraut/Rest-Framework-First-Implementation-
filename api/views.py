
from rest_framework import views, response, status
from . models import blog as BlogModel
from . import serializer as Blog_serializer
from django.forms.models import model_to_dict

# Create your views here.


class HelloAPI(views.APIView):
    serializer_class = Blog_serializer.blogseri
    def get(self, request,api_pk=None):
        if api_pk is not None:
            
            dictionary=BlogModel.objects.get(id=api_pk)
            dictionary=model_to_dict(dictionary)
            print(dictionary)
            """ for key,each in enumerate(dictionary):
                dictionary[key]={
                    "title":each.title,
                    "disc":each.desc,
                    'data':each.date
                } """
            print(type(dictionary))
        else:    
            blogmodel1 = BlogModel.objects.all()
            dictionary = {}
            for key ,each_blog in enumerate(blogmodel1):
                dictionary[key]={
                    "title":each_blog.title,
                    "details":each_blog.description,
                    'date':each_blog.date,
                }
            """ dictionary=model_to_dict(blogmodel1)  """   
            print(dictionary)
            dictionary=list(dictionary.values())
            print(dictionary)
        
        
        
        return response.Response({'data': dictionary})

    def post(self,request):

        blog_seri= self.serializer_class(data=request.data)
        if blog_seri.is_valid():
            title=blog_seri.validated_data.get('title1')
            description=blog_seri.validated_data.get('description1')
            date=blog_seri.validated_data.get('date1')
            
            blog=BlogModel.objects.create(title=title, description=description,date=date)
            print(blog)
            blog.save()
            return response.Response({'message':'Successfully submited'}) 
        else:
            return response.Response(blog_seri.errors,status=status.HTTP_400_BAD_REQUEST)   

        
