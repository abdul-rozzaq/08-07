from rest_framework.viewsets import ModelViewSet

from .models import Course, Lesson
from .permissions import IsTeacher
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsTeacher]

    def get_queryset(self):
        if self.request.user.is_teacher:
            return self.queryset.filter(teacher=self.request.user)
        return self.queryset


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsTeacher]
