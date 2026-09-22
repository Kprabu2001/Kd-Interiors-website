from django.urls import path
from .views import enquiry,home,aboutUs,contactUs,gallery,videoGallery,projectGallery,livingRoom,bedRoom,kitchen,bathRoom,homeOffice,kidsRoom,consultation


urlpatterns = [
    path("", home, name="home"),
    path("home/",home, name="home"),
    path("enquiry/", enquiry, name="enquiry"),
    path("consultation/",consultation,name="consultation"),
    path("aboutUs/",aboutUs,name="aboutUs"),
    path("contactUS/",contactUs,name="contactUs"),
    path("gallery/",gallery,name="gallery"),
    path("gallery/videoGallery",videoGallery,name="videoGallery"),
    path("gallery/projectGallery",projectGallery,name="projectGallery"),
    path("interiors/livingRoom",livingRoom,name="livingRoom"),
    path("interiors/bedRoom",bedRoom,name="bedRoom"),
    path("interiors/kitchen",kitchen,name="kitchen"),
    path("interiors/bathRoom",bathRoom,name="bathRoom"),
    path("interiors/homeOffice",homeOffice,name="homeOffice"),
    path("interiors/kidsRoom",kidsRoom,name="kidsRoom"),

]