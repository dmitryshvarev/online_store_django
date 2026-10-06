from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Product


class HomeView(TemplateView):
    template_name = "catalog/home.html"


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'category', 'price']
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'category', 'price']
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")
