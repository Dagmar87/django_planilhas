import pandas as pd
from django.shortcuts import render
from .forms import UploadPlanilhaForm
from .models import Pessoa

def importar_planilha(request):
    if request.method == 'POST':
        form = UploadPlanilhaForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            df = pd.read_excel(arquivo)

            for _, row in df.iterrows():
                Pessoa.objects.create(
                    nome=row['Nome'],
                    idade=row['Idade'],
                    cidade=row['Cidade']
                )
            return render(request, 'planilhas/sucesso.html')
        else:
            form = UploadPlanilhaForm()
            return render(request, 'planilhas/upload.html', {'form': form})