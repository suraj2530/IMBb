#import seralizer from rest framework 
from rest_framework import serializers
# from watchlist_app.models import Movie
from watchlist_app.models import WatchList,StreamPlateform, Review

class ReviewSerializer(serializers.ModelSerializer):
  review_user = serializers.StringRelatedField(read_only=True)
  class Meta:
    model = Review
    exclude = ('watchlist',)


class WatchListSerializer(serializers.ModelSerializer):
  review = ReviewSerializer(many=True, read_only=True)

  class Meta:
    model = WatchList
    fields ='__all__'

class StreamPlateformSerializer(serializers.ModelSerializer):
  watchlist = WatchListSerializer(many=True, read_only=True)  # for all
  #watchlist = serializers.StringRelatedField(many=True)    #  for title name of watchlist 
  #watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # for title name of watchlistPK of watchlist
  # watchlist = serializers.HyperlinkedRelatedField(
  #       many=True,
  #       read_only=True,
  #       view_name='movie-detail'
  #   )
  class Meta:
    model = StreamPlateform
    fields ='__all__'



# class MovieSerializer(serializers.ModelSerializer):
#   len_name = serializers.SerializerMethodField()

#   class Meta:
#     model = Movie
#     fields = ('id', 'name', 'discription', 'active','len_name')

#   def get_len_name(self, object):
#     return len(object.name)   # why passing object lec 20 at 2 min
#     # argument should accept a single argument (in addition to self), 
#     # which is the object being serialized.
  
#   def validate(self, data):
#     if data['name'] == data['discription']:
#       raise serializers.ValidationError("name and discription can't be same.")
#     return data
#   # raise error not return else bug that automatically means return btw
    

#   def validate_name(self, value):
#     if len(value) <2:
#       raise serializers.ValidationError("Name is too short")
#     return value




# def name_length(value): 
#   if len(value) < 2:
#     raise serializers.ValidationError("name is too short ")


# class MovieSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   name = serializers.CharField(validators= [name_length] )    # if there are more validators then they will be passed as validators= [name_length, name_whatever, another_validators] 
#   discription = serializers.CharField()
#   active = serializers.BooleanField()

#   def create(self, validated_data): 
#     return Movie.objects.create(**validated_data)
  
#   def update(self,instance, validated_data):
#     instance.name = validated_data.get('name', 'instace.name')
#     instance.discription = validated_data.get('discription', 'instace.discription')
#     instance.active = validated_data.get('active', 'instance.active')
#     return instance
  

#   def validate(self, data):
#     if data['name'] == data['discription']:
#       raise serializers.ValidationError("name and discription can't be same.")
#     return data
#     # raise error not return else bug that automatically means return btw
      

#   # def validate_name(self, value):
#   #   if len(value) <2:
#   #     raise serializers.ValidationError("Name is too short")
#   #   return value


