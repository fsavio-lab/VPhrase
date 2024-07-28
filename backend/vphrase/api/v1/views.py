from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Movie
from .serializers import MovieSerializer


class MovieListApiView(APIView):
    
    # No Authentication require for our case

    # List Movies
    # TODO: Provide Page based Pagination if the number of data is missing
   
    def get(self,request, *args, **kwargs):
        """
        List all Movies.
        """
        try:
            parameters : dict = dict(request.GET.items())
            movies = Movie.objects.all()

            MAX_PAGE_SIZE= 500
            page_size = MAX_PAGE_SIZE
            if "size" in parameters.keys():
                size = int(parameters['size'])
                if size < 1:
                    return Response(status.HTTP_400_BAD_REQUEST)
                if size < MAX_PAGE_SIZE:
                    page_size = int(parameters['size'])
            
            page_count = 1
            if "page" in parameters.keys():
                page_count = int(parameters['page'])

            if len(parameters) == 0:
                movie_serializer = MovieSerializer(movies.all()[:page_size], many=True)
                return Response(movie_serializer.data, status=status.HTTP_200_OK)
            
            filters = list(set(parameters.keys()) & set(MovieSerializer.Meta.fields))
            if len(filters) > 0:
                movies = movies.filter(**{k:v for k,v in parameters.items() if k in filters})

           
                    
           
            
            if "order_by" in parameters.keys():
                try:
                    field_name , sort_order = parameters["order_by"].split(" ")
                    sort_order = str(sort_order)
                    if sort_order not in ["asc","desc"]:
                        return Response(status=status.HTTP_400_BAD_REQUEST,data=sort_order)
                    elif sort_order == "desc":
                        field_name = f"-{field_name}"
                    
                    movies = movies.order_by(field_name)[page_size * (page_count - 1):page_size * page_count]
                except Exception as e:
                    return Response(status=status.HTTP_400_BAD_REQUEST,)
            # else:
            #     movies = movies.all()
            movies_serializer = MovieSerializer(movies[page_size * (page_count - 1):page_size * page_count],many=True)
            return Response(movies_serializer.data, status=status.HTTP_200_OK)

                


        except Exception as e:
            raise e
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    # We dont have a requirement to create or edit data
    # We omit post, put and patch methods.