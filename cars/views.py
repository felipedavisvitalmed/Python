from django.shortcuts import render,redirect
from cars.models import Car
from cars.forms import CarMordelForm
from django.views import View



class CarsView(View): 
     def get(self,request):
          cars = Car.objects.all().order_by('model')
          search = request.GET.get('search')
          print(search)
          if search:
               cars = Car.objects.filter(model__icontains = search).order_by('model')

          return render(
               request,
               'cars.html',
               { 'cars': cars  }
               )



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