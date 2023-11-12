from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,ListView,FormView,UpdateView,DetailView,TemplateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator 

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from cake.forms import RegistrtionForm,LoginForm,CakeCategoryForm,CakeOccationForm,CakeVarientForm
from cake.models import User,CakeCategory,CakeOccation,CakeVarient
# Create your views here.

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

def is_admin(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
            messages.error(request,"permission denied for current user!!")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

decs=[signin_required,is_admin]

class SignUpView(CreateView):
    template_name="cakes/signup.html"
    form_class=RegistrtionForm
    model=User
    success_url=reverse_lazy("signin")
    def form_valid(self, form):  #ths form_valid used to snd msges 
        #form_valid s a method used to overrdng before form save
        #get_queryset used to change queryset0.
        messages.success(self.request,"successfully signed up")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"failed to signed up")
        return super().form_valid(form)

class SignInView(FormView):
    template_name="cakes/signin.html"
    form_class=LoginForm
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login succesfully")
                return redirect("index")
            else:
                messages.error(request,"invalid credentials")
                return render(request,self.template_name,{"form":form})

@method_decorator(decs,name="dispatch")

class CategoryAddView(CreateView,ListView):
    template_name="cakes/category_add.html"
    form_class=CakeCategoryForm
    model=CakeCategory
    context_object_name="categories"
    success_url=reverse_lazy("category-add")
    def form_valid(self, form):
        messages.success(self.request,"successfully added")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"failed to add")
        return super().form_valid(form)
    def get_queryset(self):
        return CakeCategory.objects.filter(is_active=True) #actve allathath lst cheyyumbo remove avan


@signin_required
@is_admin

def remove_category(request,*args,**kwargs):
    id=kwargs.get("pk")
    CakeCategory.objects.filter(id=id).update(is_active=False)
    messages.success(request,"category removed")
    return redirect("category-add")

@method_decorator(decs,name="dispatch")

class CakeOccationCreateView(CreateView):
    template_name="cakes/occation_add.html"
    form_class=CakeOccationForm
    model=CakeOccation
    success_url=reverse_lazy("occation-add")
    def form_valid(self, form):
        messages.success(self.request,"occation added successfully")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"failed to add occation")
        return super().form_valid(form)

@method_decorator(decs,name="dispatch")

class CakeOccationListView(ListView):
    template_name="cakes/occation_list.html"
    form_class=CakeOccationForm
    model=CakeOccation
    context_object_name="cake"

@method_decorator(decs,name="dispatch")

class CakeUpdateView(UpdateView):
    template_name="cakes/occation_edit.html"
    form_class=CakeOccationForm
    model=CakeOccation
    success_url=reverse_lazy("occation-list")
    def form_valid(self, form):
        messages.success(self.request,"occation updated successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"occation updated failed")
        return super().form_invalid(form)

@signin_required
@is_admin


def remove_occationview(request,*args,**kwargs):
    id=kwargs.get("pk")
    CakeOccation.objects.filter(id=id).delete()
    return redirect("occation-list")

@method_decorator(decs,name="dispatch")

class CakeVarientCreateView(CreateView):
    template_name="cakes/cakevarient_add.html"
    form_class=CakeVarientForm
    model=CakeVarient
    success_url=reverse_lazy("occation-list")
    def form_valid(self, form):
        id=self.kwargs.get("pk")
        obj=CakeOccation.objects.get(id=id)
        form.instance.occation=obj #instance used to giving values to occation 
        messages.success(self.request,"added cake")
        return super().form_valid(form)

@method_decorator(decs,name="dispatch")

class CakeVarientDetailView(DetailView):
    template_name="cakes/cakevarient_detail.html"
    model=CakeOccation
    context_object_name="cakes"





@method_decorator(decs,name="dispatch")

class CakeVarientUpdateView(UpdateView):
    template_name="cakes/cakevarient_update.html"
    model=CakeOccation
    success_url=reverse_lazy("occation-list")
    form_class=CakeOccationForm
    def form_valid(self, form):
        messages.success(self.request,"varient updated successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"varient updated failed")
        return super().form_invalid(form)

@signin_required
@is_admin

def remove_varientview(request,*args,**kwargs):
    id=kwargs.get("pk")
    CakeVarient.objects.filter(id=id).delete()
    return redirect("occation-list")

@signin_required

def sign_out_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

class IndexView(TemplateView):
    template_name="cakes/index.html"

class TestimonialView(TemplateView):
    template_name="cakes/testimonial.html"

class ContactView(TemplateView):
    template_name="cakes/contact.html"

class ChocalateView(TemplateView):
    template_name="cakes/chocalate.html"

class AboutView(TemplateView):
    template_name="cakes/about.html"

