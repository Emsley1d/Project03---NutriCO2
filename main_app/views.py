from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipe, CustomIngredient, Ingredient, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader
from .forms import ImageTextForm, RecipeIngredients
import os
import requests
from django.utils.encoding import smart_bytes
import json
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

#RECIPES CRUD
class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name', 'image', 'upload_image_of_ingredients', 'description', 'category', 'custom_ingredients', 'method', 'user']

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = '__all__'

class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = '/recipes/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# ---------------------------------------------------------------- #
#ADD RECIPE USER MESSAGES
@login_required
def addRecipe(request):
    if request.method == "POST":
        form = RecipeCreate(request.POST)

        if form.is_valid():
            messages.success(request, 'recipe added')
            return render(request,'recipes/index.html', {'success': 'recipe added'})

        else:
            messages.error(request, 'The recipe was not saved, please try again.')
            return render(request, 'recipes/create.html', { 'error': 'The recipe was not saved, please try again.'}) 

    
    form = RecipeCreate()
    context = {'form': form}
    return render(request, 'recipes/index.html', context)

def recipes_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', { 'recipes': recipes})

@login_required
def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/detail.html', { 'recipe': recipe})

# NEW NEW NEW
@login_required
def recipe_delete(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    messages.success(request, 'Recipe deleted.')
    return render(request, 'recipes/index.html', { 'success': 'Recipe deleted'})




# CUSTOM INGREDIENTS CLASS VIEWS
class CustomIngredientList(LoginRequiredMixin, ListView):
    model = CustomIngredient
    template_name='custom_ingredients/list.html'


class CustomIngredientDetail(LoginRequiredMixin, DetailView):
    model = CustomIngredient
    template_name='custom_ingredients/detail.html'


class CustomIngredientCreate(LoginRequiredMixin, CreateView):
    model = CustomIngredient
    fields = '__all__'
    template_name='custom_ingredients/form.html'


class CustomIngredientUpdate(LoginRequiredMixin, UpdateView):
    model = CustomIngredient
    fields = '__all__'

class CustomIngredientDelete(LoginRequiredMixin, DeleteView):
    model = CustomIngredient
    success_url = '/custom_ingredients/'

# CUSTOM INGREDIENTS VIEWS
def custom_ingredients_index(request):
    custom_ingredients = CustomIngredient.objects.all()
    return render(request, 'custom_ingredients/index.html', { 'ingredients': custom_ingredients})

def custom_ingredients_detail(request, custom_ingredient_id):
    custom_ingredient = CustomIngredient.objects.get(id=custom_ingredient_id)
    return render(request, 'custom_ingredients/detail.html', { 'custom_ingredients': custom_ingredient})

# ! OLD SIGN UP METHOD
#SIGN UP USER MESSAGES
# def signup(request):
#     error_message =""
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             user = form.save()
#             login(request,user)
#             messages.success(request, 'Your registration was successful')
#             return redirect('/')
    
#         else:
#             messages.error(request, 'Your registration was unsuccessful; please try again')
#             return redirect('/')  

#     form = UserCreationForm()
#     context = {'form': form, 'error_message': error_message}
#     return render(request, 'registration/signup.html', context)

#LOGOUT USER MESSAGES
@login_required
def logout(request):
    if request.method == "POST":
        logout.is_valid()
        messages.success(request, 'You have been logged out succesfully')
        return render (request, 'home.html', {'successs': 'You have been logged out succesfully'})

#LOGIN USER MESSAGES (this one works)
def log_in(request):
    if request.method == "POST":

        if log_in.is_valid():
            messages.success(request, 'You have been logged in')
            return render(request,'home,html', {'success': 'You have been logged in'})

            # next field; create in html 

        else: 
            messages.error(request, 'We have been unable to log you in; please try again')
            return render(request, 'registration/login.html', { 'error': 'We have been unable to log you in; please try again'})


@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'password_reset_confirm.html', {'form': form})

# ---------------------------------------------------------------- #

#ASSOCIATE AND UNASSOCIATE INGREDIENTS WITH RECIPES

def assoc_ingredient(request, recipe_id, ingredient_id):
    Recipe.objects.get(id = recipe_id).ingredients.add(ingredient_id)
    return redirect('detail', recipe_id = recipe_id)

def unassoc_ingredient(request, recipe_id, ingredient_id):
    Recipe.objects.get(id = recipe_id).ingredients.remove(ingredient_id)
    return redirect('detail', recipe_id = recipe_id)

#NAV BAR
def nav_view(request):
    return render(request, "nav.html")


#USER CRUD
class UserDetail(LoginRequiredMixin, DetailView):
    model = User
    template_name='user/detail.html'
    
class UserCreate(LoginRequiredMixin, CreateView):
    model = User
    fields = '__all__'

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name='user/update.html'
    fields = '__all__'

class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name='user/user_confirm_delete.html'
    success_url = '/'

#USER DETAILS

# @login_required
# def user_detail(request, user_id):
#     user = User.objects.get(id=user_id)
#     return render(request, 'user/detail.html', { 'user': user})

# @login_required
# def user_profile(request, user_id):
#     user = User.objects.get(id=user_id)
#     return render(request, 'user/profile.html', { 'user': user})

#IMAGE TO TEXT API (100% Einar's work))
def image_to_text(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ImageTextForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('valid')
            result = {"lang": "en", "all_text": "2 tbsp extra-virgin olive oil,\nplus extra for drizzling\n300g sweet potato\n(unpeeled), cut into\n1cm cubes\n50g spring onions, trimmed\nand finely chopped\n4 eggs\n1 tsp dried thyme\n1 tsp dried oregano\n1 tsp sweet paprika\n\u00bd tsp cayenne pepper,\nplus extra to serve\n\u00bd tsp ground black pepper\n100g curly kale, stems\nremoved and leaves\nroughly chopped\n100g sweetcorn kernels\n(fresh, frozen or tinned)\n25g sunflower seeds, toasted\nand lightly crushed\nsea salt and freshly\nground black pepper\n\u314f\na\nM\nt\nF", "annotations": ["2", "tbsp", "extra", "-", "virgin", "olive", "oil", ",", "plus", "extra", "for", "drizzling", "300g", "sweet", "potato", "(", "unpeeled", ")", ",", "cut", "into", "1cm", "cubes", "50g", "spring", "onions", ",", "trimmed", "and", "finely", "chopped", "4", "eggs", "1", "tsp", "dried", "thyme", "1", "tsp", "dried", "oregano", "1", "tsp", "sweet", "paprika", "\u00bd", "tsp", "cayenne", "pepper", ",", "plus", "extra", "to", "serve", "\u00bd", "tsp", "ground", "black", "pepper", "100g", "curly", "kale", ",", "stems", "removed", "and", "leaves", "roughly", "chopped", "100g", "sweetcorn", "kernels", "(", "fresh", ",", "frozen", "or", "tinned", ")", "25g", "sunflower", "seeds", ",", "toasted", "and", "lightly", "crushed", "sea", "salt", "and", "freshly", "ground", "black", "pepper", "\u314f", "a", "M", "t", "F"]}

            # request.encoding = 'utf-8'
            # imageFile = request.FILES["image"]
            # receipt_image = imageFile.read()
            
            # url = "https://api.apilayer.com/image_to_text/upload"

            # payload = smart_bytes(receipt_image, encoding="utf-8", strings_only=False, errors="strict")
            # headers= {
            # "apikey": os.getenv('APIKEY')
            # }

            # response = requests.request("POST", url, headers=headers, data=payload)

            # status_code = response.status_code
            # result = response.text
            # print(status_code)

            # # # # MANIPULATE RESPONSE HERE
            # # # # DO CODE!!!!
            resultJSON = json.dumps(result)
            # print(resultJSON)
            return render(request, 'main_app/image_to_text.html', {'form': form, 'result': resultJSON})
            # return redirect('/')
        else:
            print('not valid')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ImageTextForm()
    return render(request, 'main_app/image_to_text.html', {'form': form})


def calculate_nutrition(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ImageTextForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('valid')

            url = "https://api.spoonacular.com/recipes/analyze"

            # Prepare payload here as JSON object
            recipe = ""

            headers= {
            "apikey": os.getenv('SPOONACULAR')
            }

            response = requests.request("POST", url, headers=headers, params=recipe)

            print(response)

            # # # # MANIPULATE RESPONSE HERE
            # return redirect('/')
        else:
            print('not valid')
    # if a GET (or any other method) we'll create a blank form
    else:
        return redirect('recipes/create/')

@login_required
def recipe_ingredients(request):
    if request.method == 'POST':
        form = RecipeIngredients(request.POST)
        print('not valid')
        if form.is_valid():
            print('valid')
            # new_feeding = form.save(commit=False)
            # new_feeding.cat_id = cat_id
            # new_feeding.save()
            return redirect('/')
        else:
            print('not valid')
    else:
        form = RecipeIngredients(request.POST)
        return render(request, 'recipes/step1.html', {'form': form})




# ! OLD SIGN UP METHOD
#SIGN UP USER MESSAGES
# def signup(request):
#     error_message =""
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             user = form.save()
#             login(request,user)
#             messages.success(request, 'Your registration was successful')
#             return redirect('/')
#         else:
#             messages.error(request, 'Your registration was unsuccessful; please try again')
#             return redirect('/')  

#     form = UserCreationForm()
#     context = {'form': form, 'error_message': error_message}
#     return render(request, 'registration/signup.html', context)