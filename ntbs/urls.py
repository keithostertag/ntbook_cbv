from django.conf.urls import url

from ntbs import views

urlpatterns = [
  url(r'^new$', views.NtbookCreate.as_view(), name='ntbook_new'),
  url(r'^edit/(?P<pk>\d+)$', views.NtbookUpdate.as_view(), name='ntbook_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.NtbookDelete.as_view(), name='ntbook_delete')
]
