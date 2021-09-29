
from functools import partial
from django.core.checks import messages
from django.core.validators import validate_email
from rest_framework import views, response, status,viewsets
from rest_framework.serializers import Serializer
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



    def put(self,request,api_pk):
        blog_seri=self.serializer_class(data=request.data)
        dbobject=BlogModel.objects.get(id=api_pk)
        if blog_seri.is_valid():
            title=blog_seri.validated_data.get('title1')
            description=blog_seri.validated_data.get('description1')
            date=blog_seri.validated_data.get('date1')
            dbobject.title=title
            dbobject.description=description
            dbobject.date=date
            dbobject.save()
            print(dbobject)
            return response.Response({'message':'Successfully updated object'}) 
        else:
            return response.Response(blog_seri.errors,status=status.HTTP_400_BAD_REQUEST) 
        
            

    def patch(self,request,api_pk):
        
        if api_pk is not None:
            dbobject=BlogModel.objects.get(id=api_pk)
            blog_seri=self.serializer_class(dbobject,data=request.data,partial=True)
            if blog_seri.is_valid():
                title=blog_seri.validated_data.get('title1')
                description=blog_seri.validated_data.get('description1')
                date=blog_seri.validated_data.get('date1')
                if title is not None:
                    dbobject.title=title
                if description is not None: 
                    dbobject.description=description   
                if date is not None:
                    dbobject.date=date
                dbobject.save()
                return response.Response({'message':"succesfully Updated partial value"})
            else:
                return response.Response(blog_seri.errors,status=status.HTTP_400_BAD_REQUEST)        
        else:
            return response.Response({"message":"pk is required "})

    def delete(self,request,api_pk=None):
        if api_pk:
            dbobject=BlogModel.objects.get(id=api_pk).delete()
            
            return response.Response({"message":'Succesfuly deleted'})
        else:
            return response.Response({"pk is required!!"})

class hello(views.APIView):
    serializer_class=Blog_serializer.blogseri
    def get(self,request):
        blogmodel=BlogModel.objects.all()
        print(blogmodel)
        dict={}
        for key,each in enumerate(blogmodel):
            dict[key]={
                "title":each.title,
                "desc:":each.description,
                "date":each.date
            }
        dict=list(dict.values())    
        print(dict)    
        return response.Response({"data":dict})
    def post(self,request):
        blog_seri=self.serializer_class(data=request.data)
        if blog_seri.is_valid():
            title1=blog_seri.validated_data.get("title1")
            obj=BlogModel()
            obj.title=title1
            obj.save()
            print(obj)
        else:
            return response.Response({"message":"error"})    
        return response.Response("successfully updated")    
    
# class HelloApi_viewsets(viewsets.ViewSet):
#     serializer=Blog_serializer.blogseri
#     def list(self,request):
        
#         printname=['this is is msg printing for the utility']
#         return response.Response(printname)

#     def create(self,request):
#         blog_seri=self.serializer(data=request.data)
#         if blog_seri.is_valid():
            
            

       

