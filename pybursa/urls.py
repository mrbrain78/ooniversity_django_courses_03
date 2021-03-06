from django.conf.urls import patterns, include, url, handler404, handler500
from django.contrib import admin

from pybursa import views
from feedbacks.views import FeedbackView

handler404 = 'pybursa.views.page_not_found'
handler500 = 'pybursa.views.server_error'

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^feedback/', FeedbackView.as_view(), name = "feedback"),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^student_list/', views.student_list, name='student_list'),
    url(r'^student_detail/', views.student_detail, name='student_detail'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^courses/', include('courses.urls', namespace="courses")),    
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
)
