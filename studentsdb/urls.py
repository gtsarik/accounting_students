from django.conf.urls import patterns, include, url
from django.contrib import admin

from students.views.students import StudentCreateView, StudentUpdateView, StudentDeleteView
from students.views.groups import GroupAddView, GroupUpdateView, GroupDeleteView
from students.views.journal import JournalView

from .settings import MEDIA_ROOT, DEBUG

urlpatterns = patterns('',
    # Students urls
    url(r'^$', 'students.views.students.students_list', name='home'),
    # url(r'^students/add/$', 'students.views.students.students_add', name='students_add'),
    url(r'^students/add/$', StudentCreateView.as_view(), name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),

    # Groups urls
    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
    url(r'^groups/add/$', GroupAddView.as_view(), name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdateView.as_view(),
         name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', GroupDeleteView.as_view(),
         name='groups_delete'),

    # Journal urls
    url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),

    # Contact Admin Form
    url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin',
        name='contact_admin'),

    # Admin urls
    url(r'^admin/', include(admin.site.urls)),

)

if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT}))
