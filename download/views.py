from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import UrlForm
from django.http import HttpResponseRedirect
import pafy


# Create your views here.
class HomePageView(FormView):
    template_name = 'home.html'
    form_class = UrlForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        data = form.cleaned_data
        try:
            p = pafy.new(data['video_link'])
            title = p.title
            author = p.author
            if data['video_type'] == 'mp4':
                best = p.getbest(preftype=data['video_type'])
            else:
                best = p.getbestaudio(preftype=data['video_type'])
            url = best.url
            context = {
                'title': title,
                'author': author,
                'url': url,
                'extension': data['video_type']
            }
            print(context)
            return render(self.request, 'success.html', context)
        except Exception as e:
            print(e)
            return HttpResponseRedirect(self.success_url)
