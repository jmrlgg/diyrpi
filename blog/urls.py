"""blog.app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'), #home
    url(r'^news/$', views.blog_post, name='news'), #blog post
]
    # url(r'^members/$', users, name='users'),  # View of current members under Blogger(model)
    # url(r'^news/$', entry, name='news'),  # Post entry view [ entire Entry(model) ]
    # url(r'^post/new/$', post_new, name='post_new'),  # create new post if logged_in
    # url(r'^base/$', base),
    # url(r'^contact/$', contact),  # simple form with contact abilities ref. email
    # url(r'^contactpopup/$', contact_popup),  # (in development) test run for [contact us] to be inside a " bootstrap modal "
    # url(r'^$', home),  # home
