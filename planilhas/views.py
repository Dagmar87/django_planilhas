import pandas as pd
from django.shortcuts import render, redirect
from .forms import UploadPlanilhaForm
from .models import Pessoa

def importar_planilha(request):
    if request.method == 'POST':
        form = UploadPlanilhaForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            try:
                df = pd.read_excel(arquivo)
                
                # Convert column names to match your model fields
                df_columns = {col.lower(): col for col in df.columns}
                
                for _, row in df.iterrows():
                    Pessoa.objects.create(
                        nome=row[df_columns.get('nome', 'Nome')],
                        idade=row[df_columns.get('idade', 'Idade')],
                        cidade=row[df_columns.get('cidade', 'Cidade')]
                    )
                return render(request, 'planilhas/sucesso.html')
            except Exception as e:
                # Handle any errors during file processing
                return render(request, 'planilhas/upload.html', {
                    'form': form,
                    'error': f'Erro ao processar o arquivo: {str(e)}'
                })
    else:
        form = UploadPlanilhaForm()
    
    return render(request, 'planilhas/upload.html', {'form': form})