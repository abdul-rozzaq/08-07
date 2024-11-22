from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Course, Lesson

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_teacher", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data["username"], email=validated_data["email"], password=validated_data["password"], is_teacher=validated_data.get("is_teacher", False))
        return user


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Course
        fields = ["id", "name", "description", "price", "teacher"]

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["teacher"] = request.user
        return super().create(validated_data)


class LessonSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()

    class Meta:
        model = Lesson
        fields = ["id", "title", "content", "course"]
