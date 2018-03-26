from django.conf.urls import url, include
from blog import views

app_name = 'blog'

urlpatterns = [

url(r'^$',views.post_list,name='post_list'),
url(r'^post/(?P<pk>\d+)$',views.post_detail,name='post_detail'),
url(r'^post/edit/(?P<pk>\d+)$',views.post_update,name='post_update'),
url(r'^post/create/$',views.post_create,name='post_create'),
url(r'^post/delete/(?P<pk>\d+)$',views.PostDeleteView.as_view(),name='post_delete'),
url(r'^drafts/$',views.draft_list,name='draft_list'),
url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),

]
