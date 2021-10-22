from django import urls
from django.urls  import path, include
# from watchlist_app.api.views import MovieListAV, MovieDetailAV
# from watchlist_app.api.views import movie_list  , movie_details
from watchlist_app.api.views import ( ReviewCreate, ReviewDetail, ReviewList,
                                  WatchListAV , WatchDetailAV, StreamPlateformAV,
                                   StreamPlateformDetailAV )
from watchlist_app.api.views import StreamPlateformVS

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlateformVS, basename='stream')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'), 
    path('', include(router.urls)),
    # path('stream/', StreamPlateformAV.as_view(),name='streamplatform-list'),
    # path('stream/<int:pk>/', StreamPlateformDetailAV.as_view(), name='streamplateform-detail'),
 
    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),  # accessing idividual review
    
    
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail')

    #  path("list/", MovieListAV.as_view(), name="movie-list"),
    #  path("<int:pk>/", MovieDetailAV.as_view(),name="movie-detail"), 

    # path("list/", movie_list, name="movie-list"), 
    # path("<int:pk>/", movie_details, name="movie-detail"),   # mind this pk thing the way 
    

    


]
