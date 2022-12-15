from rest_framework import serializers
from .models import Review
from user.serializers import TinyUserSerializer


class ReviewSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer()

    class Meta:
        model = Review
        fields = {

            "user",
            "payload",
            "rating",


        }
