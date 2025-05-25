from django.shortcuts import render,redirect
from cars.models import Car
from cars.forms import CarMordelForm
from django.views import View
from django.views.generic import ListView,CreateView



class CarsView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(model__icontains=search).order_by('model')
        return queryset
    


class NewCarView(View):
    template_name = 'new_car.html'

    def render_form(self, request, form):
        """Método auxiliar para renderizar o formulário."""
        return render(request, self.template_name, {'new_car_form': form})

    def get(self, request):
        new_car_form = CarMordelForm()
        return self.render_form(request, new_car_form)

    def post(self, request):
        new_car_form = CarMordelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return self.render_form(request, new_car_form)
    


class NewCarCreateView(CreateView):
    model = Car
    form_class = CarMordelForm
    template_name = 'new_car.html'
    success_url = '/new_car/'

