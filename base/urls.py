


from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('bachdegree/',views.bachdegree,name='bachdegree'),
    path('mastersdegree/',views.mastersdegree,name='mastersdegree'),
    path('iot/',views.iot,name='iot'),
    path('nursing/',views.nursing,name='nursing'),
    path('business/',views.business,name='business'),
    path('engineering/',views.engineering,name='engineering'),
    path('about/',views.about,name='about'),
    path('applyinfo/',views.applyinfo,name='applyinfo'),
    path('jointapp/',views.jointapp,name='jointapp'),
    path('directapp/',views.directapp,name='directapp'),
    path('eligibility/',views.eligibility,name='eligibility'),
    path('studyplace/',views.studyplace,name='studyplace'),
    path('infostudents/',views.infostudents,name='infostudents'),
    path('howdirect/',views.howdirect,name='howdirect'),
    path('directselection/',views.directselection,name='directselection'),
    path('directfees/',views.directfees,name='directfees'),
    path('scholarship/',views.scholarship,name='scholarship'),
    path('howjoint/',views.howjoint,name='howjoint'),
    path('jointselection/',views.jointselection,name='jointselection'),
    path('jointfees/',views.jointfees,name='jointfees'),
    path('digitalhealth/',views.digitalhealth,name='digitalhealth'),
    path('energy/',views.energy,name='energy'),
    path('howmasters/',views.howmasters,name='howmasters'),
    path('masterfees/',views.masterfees,name='masterfees'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact/',views.contact,name='contact'),
    path('applicationform/',views.applicationform,name='applicationform'),
]
