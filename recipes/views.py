from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Recipe

"""return the list of the recipes 
in ascending order with the newest recipe entry on top of the list"""


class RecipeListView(ListView):
    model = Recipe
    queryset = Recipe.objects.all().order_by("-date_created")


"""Connect the class to the Recipe model"""


class RecipeDetailView(DetailView):
    model = Recipe


"""Perfoms the action of creating a recipe item"""


class RecipeCreateView(SuccessMessageMixin, CreateView):
    model = Recipe
    fields = ["name", "comments", "ingredients", "preparation"]
    """With reverse_lazy the user will be redirected in index page
     after the creation of the recipe"""
    success_url = reverse_lazy("recipe-list")
    success_message = "Your new recipe was added!"


"""Update the contents of a recipe.
With reverse_lazy the user will be redirected in the
 recipe_detail page of the recipe after editing it"""


class RecipeUpdateView(SuccessMessageMixin, UpdateView):
    model = Recipe
    fields = ["name", "comments", "ingredients", "preparation"]
    success_message = "Your recipe was updated!"

    def get_success_url(self):
        return reverse_lazy("recipe-detail", kwargs={"pk": self.object.pk})


""" Performs the action of deleting a recipe item, so you don’t need 
to define any fields in it.With reverse_lazy the user will be redirected 
in the index page after the deletion of the recipe"""


class RecipeDeleteView(SuccessMessageMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipe-list")
    success_message = "Your recipe was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
