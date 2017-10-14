from django.conf.urls import url

from ntbs import views

urlpatterns = [
  # url(r'^$', views.NtbookList.as_view(), name='ntb_list'),
  url(r'^new$', views.NtbookCreate.as_view(), name='ntbook_new'),
  url(r'^edit/(?P<pk>\d+)$', views.NtbookUpdate.as_view(), name='ntb_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.NtbookDelete.as_view(), name='ntb_delete')
]
