from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse

from core.models import Course, CourseContent, CourseMember, User

# Create your views here.
def allCourse(request):
    courses = Course.objects.all().select_related('teacher')
    data_resp = []
    for course in courses:
        record = {'id': course.id,
                  'name':  course.name,
                  'price': course.price,
                  'teacher': {
                      'id': course.teacher.id,
                      'username': course.teacher.username,
                      'fullname': f"{course.teacher.first_name} {course.teacher.last_name}"
                      }}
        data_resp.append(record)

    return JsonResponse(data_resp, safe=False)

def userProfile(request, user_id):
    user = User.objects.get(pk=user_id)
    courses = Course.objects.filter(teacher=user)
    data_resp = {
        'username': user.username,
        'email': user.email,
        'fullname': f"{user.first_name} {user.last_name}"
    }
    data_resp['courses'] = []
    for course in courses:
        course_data = {'id': course.id,
                       'description':  course.description,
                       'price': course.price,
                       }
        data_resp['courses'].append(course_data)
    
    return JsonResponse(data_resp, safe=False)

from django.db.models import Count, Min, Max, Avg

def courseStats(request):
    courses = Course.objects.all()
    statistic = courses.aggregate(
        course_count=Count('*'),
        min_price=Min('price'),
        max_price=Max('price'),
        avg_price=Avg('price')
    )
    cheapest_list = Course.objects.filter(price=statistic['min_price'])
    expensive_list = Course.objects.filter(price=statistic['max_price'])
    popular_list = Course.objects.annotate(member_count=Count('coursemember'))\
        .order_by('-member_count')[:3]
    unpopular_list = Course.objects.annotate(member_count=Count('coursemember'))\
        .order_by('member_count')[:3]

    data_resp = {
        'course_count': statistic['course_count'],
        'min_price': statistic['min_price'],
        'max_price': statistic['max_price'],
        'avg_price': statistic['avg_price'],
        'cheapest': [course.name for course in cheapest_list],  # Convert to list
        'expensive': [course.name for course in expensive_list],  # Convert to list
        'popular': [course.name for course in popular_list],  # Convert to list
        'unpopular': [course.name for course in unpopular_list],  # Convert to list
    }

    return JsonResponse(data_resp, safe=False)
