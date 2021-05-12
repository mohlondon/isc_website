from rest_framework import serializers
from .models import Event, Commenters, Likes
from materials.models import Material
from Users.models import CustomUser
#from easy_thumbnails.templatetags.thumbnail import thumbnail_url
from materials.serializers import MaterialSerializer


#class ThumbnailSerializer(serializers.ImageField):
#    def __init__(self, alias, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.read_only = True
#        self.alias = alias
#
#    def to_representation(self, value):
#        if not value:
#            return None
#        url = thumbnail_url(value, self.alias)
#        request = self.context.get('request', None)
#        if request is not None:
#            return request.build_absolute_uri(url)
#        return url

class CustomUserSerializer(serializers.ModelSerializer):
#    Picture = ThumbnailSerializer(alias="avatar")

    class Meta:
        model = CustomUser
        fields = ['Picture', 'username', 'id', "gender"]


class CommentersSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Commenters
        exclude = []


class LikesSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Likes
        exclude = []


class EventsSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    comments = CommentersSerializer(source='commenters_set', many=True)
    likes = CommentersSerializer(source='likes_set', many=True)
#    Picture = ThumbnailSerializer(alias="post")
    material = MaterialSerializer(many=True)

    class Meta:
        model = Event
        fields = ['id', "user", "Picture", "description", "material",
                  "title", "place", "likes", 'Coach', "comments", "created_at", "updated_at"]
