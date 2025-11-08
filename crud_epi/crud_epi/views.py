from django.shortcuts import render

def pagina_inicial(request):
    # Lógica para buscar dados no banco de dados, se necessário
    return render(request, 'index.html', contexto)