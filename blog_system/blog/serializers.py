from rest_framework import serializers
from .models import Blog, CustomUser
from rest_framework.validators import ValidationError


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','user', 'title', 'description', 'published_date',
                  'last_updated_on', 'approval_status',]
        read_only_fields = ('user','approval_status')

    ## To show fields of user in response insted of user id
    #def to_representation(self, instance):
        #self.fields["user"] = CustomUserSignupSerializer(read_only=True)
        #return super(BlogSerializer, self).to_representation(instance)

    def create(self, validated_data):
        """
        Return blog with assigning current authenticated user object to user field.
        """
        username = self.context.get('request').user
        user_obj = CustomUser.objects.get(username=username)

        title = validated_data.get('title')
        description = validated_data.get('description')
        published_date = validated_data.get('published_date')
        last_updated_on = validated_data.get('last_updated_on')

        blog = Blog(title=title, description=description,
                    published_date=published_date,
                    last_updated_on=last_updated_on)
        blog.user = user_obj
        blog.save()
        return blog


class CustomUserSignupSerializer(serializers.ModelSerializer):
    #confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['id','username', 'password',
                  'email', 'gender', 'mob_number', 'city']

    def validate_mob_number(self, mob_number):
        if len(str(mob_number)) <= 10:
            raise ValidationError(
                        'Please enter country code also. Ex. 919028890852'
                        )

    def create(self, validated_data):
        """
        Text formated password converted in hash format and returns user.
        """
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        gender = validated_data['gender']
        mob_number = validated_data['mob_number']
        city = validated_data['city']

        user = CustomUser(username=username, email=email, gender=gender,
                          mob_number=mob_number, city=city)
        user.set_password(password)
        user.save()
        return user
