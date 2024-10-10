from django.shortcuts import render
from django.template.loader import render_to_string
from prosite import views as pviews

class CustomContext():
    
    def __init__(self, *args, **kwargs):
        super(CustomContext, self).__init__(*args, **kwargs)
    
        
class Tab():
    
    def __init__(self, id:str, name:str, template:str, context=None) -> None:
        self.id         = id 
        self.name       = name
        self.template   = template
        self.context    = context
        
      
def index(request):
    tabs = [
        Tab('prosite',  'PROSITE motif pattern',        'prosite/home.html', pviews.context),
        Tab('frequency','Frequency matrix calculator',  'frequency/home.html',  'Frequency matrix calculator')
    ]
    
    context = {
        "tabs": tabs,
        "index_title" : "BIOINFORMÁTICA ESTRUTURAL",
    }
    return render(request, 'index.html', context)