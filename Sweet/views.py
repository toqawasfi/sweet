from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snack
# Create your views here.

class SnackListView(ListView):
    template_name='sweet/snacks_list.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name="sweet/snacks_detail.html"
    model= Snack

class SnackCreateView(CreateView):
    template_name="sweet/snacks_create.html"
    model= Snack
    fields=['title', 'description', 'purchaser']

class SnackUpdateView(UpdateView):
    template_name="sweet/snacks_update.html"
    model= Snack
    fields=['title', 'description', 'purchaser']

class SnackDeleteView(DeleteView):
    template_name='sweet/snacks_delete.html'
    model= Snack
    success_url=reverse_lazy('snacks_list')