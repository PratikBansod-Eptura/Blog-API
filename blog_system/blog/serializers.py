from rest_framework import serializers
from .models import Blog, CustomUser


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','user', 'title', 'description', 'published_date', 'published_date', 'last_updated_on', 'approval_status',]


class CustomUserSignupSerializer(serializers.ModelSerializer):
    #confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['id','username', 'password', 'email', 'gender', 'mob_number', 'city']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        gender = validated_data['gender']
        mob_number = validated_data['mob_number']
        city = validated_data['city']

        user = CustomUser(username=username, email=email, gender=gender, mob_number=mob_number, city=city)
        user.set_password(password)
        user.save()
        return user
