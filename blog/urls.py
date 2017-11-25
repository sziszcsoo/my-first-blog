from django.conf.urls import url
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^favicon.ico$',
            RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'),
            permanent=False),
            name="favicon"
        ),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]
