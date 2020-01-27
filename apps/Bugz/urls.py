from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^contact$', views.contact),
    url(r'^about$', views.about),
    url(r'^login$', views.login),
    url(r'^process_inquery$', views.process_inquery),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^register_admin_process$', views.register_admin_process),
    url(r'^login_process$', views.login_process),
    url(r'^add_project$', views.add_project),
    url(r'^dashboard$', views.dashboard),
    url(r'^project_report$', views.project_report),
    url(r'^add_bug$', views.add_bug),
    url(r'^bug_report$', views.bug_report),
    url(r'^add_user$', views.add_user),
    url(r'^user_report$', views.user_report),
    url(r'^add_project_process$', views.add_project_process),
    url(r'^add_bug_process$', views.add_bug_process),
    url(r'^add_user_process$', views.add_user_process),

]