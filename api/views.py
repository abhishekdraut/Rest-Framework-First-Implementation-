
from functools import partial
from django.core.checks import messages
from django.core.validators import validate_email
from django.db.models.query import QuerySet
from rest_framework import views, response, status,viewsets
from rest_framework.serializers import Serializer
from . models import blog as BlogModel
from . import serializer as Blog_serializer
from django.forms.models import model_to_dict

# Create your views here.
# Prper way to create the api views just addition of serializers and their validator are increase.

class HelloAPI(views.APIView):
    serializer_class = Blog_serializer.blogseri                                #first add your serializer to serializer_Class
    
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
            # dictionary=model_to_dict(blogmodel1)    
            print(dictionary)
            dictionary=list(dictionary.values())
            print(dictionary)
            
        
        
        
        return response.Response({'data':dictionary})

    def post(self,request):

        blog_seri= self.serializer_class(data=request.data)     #second pass the request data to serializer and use that data through 
        print(request)                                                       #validator .is valid() is must to fetch data from serializer is usnig 
                                                                # data= in serailizer class.        
        if blog_seri.is_valid():
            title=blog_seri.validated_data.get('title')        #extraction of validated data.
            description=blog_seri.validated_data.get('description')
            date=blog_seri.validated_data.get('date')
            
            blog=BlogModel.objects.create(title=title, description=description,date=date)
            print(blog)
            blog.save()
            return response.Response({'message':'Successfully submited'}) 
        else:
            return response.Response(blog_seri.errors,status=status.HTTP_400_BAD_REQUEST)  



    def put(self,request,api_pk):                                        # pk is need to update the particular data in api views.
        blog_seri=self.serializer_class(data=request.data)               # evry time you have to pass the data through serializers.
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

class Viewset(viewsets.ViewSet):
    serializer_class=Blog_serializer.blogseri    #defined serializer in serailizer_class is mendatory step.

    def list(self ,request):                       
        queryset=BlogModel.objects.all()                             #import data for DB
        serialize=self.serializer_class(queryset,many=True)          #pass imported object in serializer .(many objects are coming from DB)
        print(serialize.data)

        return response.Response(serialize.data)


    def retrieve(self,request,pk=None):                         #retrieve used to fetch single object from Db

        queryset=BlogModel.objects.get(pk=pk)
        serialize=self.serializer_class(queryset)
        print(serialize.data)
                
        return response.Response(serialize.data)


    def create(self,request):                                   #create used to creete the new object at db
        serialize=self.serializer_class(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        
        
        return response.Response("create!!") 

       

