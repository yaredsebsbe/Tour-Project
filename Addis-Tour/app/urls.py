from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('package',views.package,name='package'),
    path('createPackage',views.create_package,name='createPackage'),
    path('search',views.search,name='search'),
    path('guides',views.guides,name='guides'),
    path('guideReg',views.guideReg,name='guideReg'),
    path('guideLog',views.guideLog,name='guideLog'),
    path('forget_q',views.guideV,name='forget_q'),
    path('guideForget',views.guideForget,name='guideForget'),
    path('deleter',views.deleter,name='deleter'),
    path('logout',views.logout,name='logout'),
    path('list_package',views.list_package,name="list_package"),
    path('redirLog',views.redirLog,name="redirLog"),
    path('redirSign',views.redirSign,name="redirSign"),
    path('booked',views.booked,name="booked"),
    path('book',views.book,name="book"),
]