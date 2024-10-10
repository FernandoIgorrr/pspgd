from django.shortcuts import render
from .forms import FastaUploadForm

# Create your views here.

@staticmethod
def context():
    return {
        'title'     : 'PROSITE signature pattern processor',
        'sub_title' : 'Selecione um arquivo de proteínas alinhadas no formato fasta',
        'form'      : FastaUploadForm()
    }

def home(request) -> render:
    title = "PROSITE signature pattern processor"  
    #processed_data = None
    
    # if request.method == 'POST' and 'file' in request.FILES:
        # uploaded_file = request.FILES['file']
        
        # Processa o arquivo
        # processed_data = process_file(uploaded_file)
    context = {
        'title': title
    }
    
    
    # Passa o título e os dados processados para o template
    return render(
        request, 
        'home.html',
        context    
    )
