from rest_framework.decorators import api_view
from rest_framework.response import Response
# from watchlist_app.models import Movie
# from watchlist_app.api.serializers import MovieSerializer
from rest_framework import status
from rest_framework.views import APIView
from watchlist_app.models import WatchList,StreamPlateform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlateformSerializer, ReviewSerializer
from rest_framework import mixins
from rest_framework import generics, viewsets
from django.shortcuts import get_object_or_404 
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from watchlist_app.api import permissions 


class StreamPlateformVS(viewsets.ModelViewSet):
  queryset = StreamPlateform.objects.all()
  serializer_class = StreamPlateformSerializer

# class StreamPlateformVS(viewsets.ReadOnlyModelViewSet):
#   queryset = StreamPlateform.objects.all()
#   serializer_class = StreamPlateformSerializer


# class StreamPlateformVS(viewsets.ViewSet):

#     def list(self, request):
#         queryset = StreamPlateform.objects.all()
#         serializer = StreamPlateformSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlateform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlateformSerializer(watchlist)
#         return Response(serializer.data)

#     def create(self, request):
#       serializer = StreamPlateformSerializer(data = request.data)
#       if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status = status.HTTP_201_CREATED)
#       else: 
#         return Response(serializer.errors)




class ReviewList(generics.ListAPIView):
  # queryset = Review.objects.all()
  serializer_class = ReviewSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
      pk = self.kwargs['pk']     # taking pk input in browser 
      return Review.objects.filter(watchlist = pk)

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    # throttle_classes = [ReviewCreateThrottle]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie!")
            
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2

        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()

        serializer.save(watchlist=watchlist, review_user=review_user)

# class ReviewCreate(generics.CreateAPIView):
#     serializer_class = ReviewSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get_queryset(self):
#         return Review.objects.all()

#     def perform_create(self, serializer):
#         pk = self.kwargs.get('pk')
#         watchlist = WatchList.objects.get(pk=pk)

#         review_user = self.request.user
#         review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)

#         if review_queryset.exists():
#             raise ValidationError("You have already reviewed this movie!")
#         if watchlist.number_rating == 0:
#           watchlist.avg_rating = serializer.validated_data["rating"]
#         else:
#           watchlist.avg_rating = ( watchlist.avg_rating + serializer.validated_data["rating"])/2
#         watchlist.number_rating = watchlist.number_rating + 1
        

#         serializer.save(watchlist=watchlist, review_user=review_user)

    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
  permission_classes = [permissions.ReviewOwnerOrReadOnly]



# class ReviewDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
#   queryset = Review.objects.all()
#   serializer_class = ReviewSerializer

#   def get(self, request, *args, **kwargs):
#     return self.retrieve(request, *args, **kwargs)


# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class WatchListAV(APIView):
  def get(self, request):
    watchlist = WatchList.objects.all()
    serializer = WatchListSerializer(watchlist, many=True, context={'request': request}) 
    return Response(serializer.data) 

  def post(self, request):
    watchlist = WatchList.objects.all()
    serializer = WatchListSerializer(data= request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else: 
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatchDetailAV(APIView):
  def get(self, request,pk):
    watchlist = WatchList.objects.get(pk=pk)
    serializer = WatchListSerializer(watchlist, context={'request': request}) 
    return Response(serializer.data) 

  def put(self, request,pk):
    watchlist = WatchList.objects.get(pk=pk)
    serializer = WatchListSerializer(watchlist, data=request.data)  
    if serializer.is_valid():
      return Response(watchlist.data)
  
  def delete(self,request, pk):
    watchlist = WatchList.objects.get(pk=pk)
    watchlist.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)

class StreamPlateformAV(APIView):
  def get(self,request):
    plateform = StreamPlateform.objects.all()
    serializer = StreamPlateformSerializer(plateform, many=True, context={'request': request})
    return Response(serializer.data, status = status.HTTP_200_OK)


  def post(self,request):
    serializer = StreamPlateformSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status = status.HTTP_201_CREATED)
    else: 
      return Response(serializer.errors)

  

class StreamPlateformDetailAV(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlateform.objects.get(pk=pk)
        except StreamPlateform.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlateformSerializer(
            platform, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamPlateform.objects.get(pk=pk)
        serializer = StreamPlateformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = StreamPlateform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class StreamPlateformDetailAV(APIView):

#   def get(self,request,pk):
#     try:
#       plateform = StreamPlateform.objects.get(pk=pk)
#     except StreamPlateform.DoesNotExist:
#       return Response({'error': 'Not Found'}, status = status.HTTP_404_NOT_FOUND)
#     serializer = StreamPlateformSerializer(plateform, context={'request': request} )
#     return Response(serializer.data)

#   def put(self,request,pk):
#     plateform = StreamPlateform.objects.get(pk=pk)
#     serializer = StreamPlateformSerializer(plateform, data= request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response({'success': 'OK'}, status = status.HTTP_200_OK)
#     else: 
#       return Response({'error': 'Invalid Request'}, status = status.HTTP_400_BAD_REQUEST)

#   def delete(self,request,pk):
#     plateform  = StreamPlateform.objects.get(pk=pk)
#     plateform.delete()
#     return Response({'error': 'Delete'}, status = status.HTTP_204)

  


# class MovieListAV(APIView):
#   def get(self, request):
#     movie = Movie.objects.all()
#     serializer = MovieSerializer(movie, many=True) 
#     return Response(serializer.data) 

#   def post(self, request):
#     movie = Movie.objects.all()
#     serializer = MovieSerializer(data= request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else: 
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class MovieDetailAV(APIView):

#   def get(self, request, pk):
#     try:      
#       movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#       return Response({'Error': 'Movie not found.'} , status=status.HTTP_404_NOT_FOUND)
#     serializer = MovieSerializer(movie)
#     return Response(serializer.data, status=status.HTTP_200_OK)

#   def put(self, request, pk):
#     movie = Movie.objects.get(pk=pk)
#     serializer = MovieSerializer(movie, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_200_OK)
#     else:
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#   def delete(self, request, pk):
#     movie = Movie.objects.get(pk=pk)
#     movie.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def movie_list(request): 
#   if request.method == 'GET':
#     movie = Movie.objects.all()
#     serializer = MovieSerializer(movie, many=True) # many = True else getting query_set error 
#     return Response(serializer.data) 

#   if request.method == 'POST':
#     serializer = MovieSerializer(data=request.data) # data = request.data not request.POST
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status = status.HTTP_201_CREATED)
#     else :
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE']) 
# def movie_details(request,pk):
#   if request.method == 'GET':
#     try:      # now working try catch get me lagao or main me like docs in drf tut 2
#       movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#       return Response({'Error': 'Movie not found.'} , status=status.HTTP_404_NOT_FOUND)
#     serializer = MovieSerializer(movie)
#     return Response(serializer.data, status=status.HTTP_200_OK)
    
  
#   if request.method == 'PUT':
#     movie = Movie.objects.get(pk=pk)
#     serializer = MovieSerializer(movie, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_200_OK)
#     else:
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
#   if request.method == 'Delete':
#     movie = Movie.objects.get(pk=pk)
#     movie.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT) 
#     # not working
   