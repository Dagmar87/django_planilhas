# Django Planilhas

Um projeto Django para gerenciamento de planilhas.

## 🚀 Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes do Python)
- Virtualenv (recomendado)

## 🛠️ Instalação

1. Clone o repositório:
   ```bash
   git clone [URL_DO_REPOSITÓRIO]
   cd django_planilhas
   ```

2. Crie e ative o ambiente virtual (recomendado):
   ```bash
   # No Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # No Linux/MacOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```

5. Crie um superusuário (opcional):
   ```bash
   python manage.py createsuperuser
   ```

6. Execute o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

7. Acesse o projeto em [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📁 Estrutura do Projeto

```
django_planilhas/
├── planilha_config/     # Configurações do projeto Django
├── planilhas/           # Aplicativo principal
├── manage.py            # Script de gerenciamento do Django
└── README.md            # Este arquivo
```

## 🔧 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
DEBUG=True
SECRET_KEY=sua_chave_secreta_aqui
```

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
