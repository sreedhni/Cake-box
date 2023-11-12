from django.contrib import admin
from django.urls import path
from cake.views import SignInView,SignUpView,CategoryAddView,remove_category,CakeOccationCreateView,CakeOccationListView,CakeUpdateView,remove_occationview,CakeVarientCreateView,CakeVarientDetailView,CakeVarientUpdateView,remove_varientview,sign_out_view,IndexView,ContactView,ChocalateView,TestimonialView,AboutView

urlpatterns=[
    path("signup",SignUpView.as_view(),name="signup"),
   path("signin",SignInView.as_view(),name="signin"),
   path("index/",IndexView.as_view(),name="index"),
   path("contact/",IndexView.as_view(),name="contact"),
   path("choclate/",IndexView.as_view(),name="choclate"),
   path("about/",IndexView.as_view(),name="about"),
    path("testimo/",IndexView.as_view(),name="test"),



   path("signout",sign_out_view,name="signout"),
   path("category/add",CategoryAddView.as_view(),name="category-add"),
   path("categories/<int:pk>/remove",remove_category,name="remove-category"),
   path("occation/add",CakeOccationCreateView.as_view(),name="occation-add"),
   path("occation/all",CakeOccationListView.as_view(),name="occation-list"),
   path("occation/<int:pk>/change",CakeUpdateView.as_view(),name="occation-change"),
   path("occation/<int:pk>/remove",remove_occationview,name="occation-remove"),
   path("cake/<int:pk>/varients/add",CakeVarientCreateView.as_view(),name="add-varient"),
   path("cake/<int:pk>/",CakeVarientDetailView.as_view(),name="detail-varient"),
   path("cake/<int:pk>/change",CakeVarientUpdateView.as_view(),name="edit-varient"),
   path("cake/<int:pk>/remove",remove_varientview,name="remove-varient"),
   



]