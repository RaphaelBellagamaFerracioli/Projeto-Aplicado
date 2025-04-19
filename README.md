# 🛒 Central de Preços
Este é um projeto Django para gerenciar e exibir informações de preços de produtos.
Ele está estruturado com um app principal chamado `app_central_precos`.

## 🚀 Como rodar o projeto localmente

Siga os passos abaixo para executar o projeto em sua máquina:

### ✅ 1. Clone o repositório

bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio/central_precos


### ✅ 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
```

- **Windows:**

```bash
.\venv\Scripts\activate
```

- **Linux/MacOS:**

```bash
source venv/bin/activate
```

### ✅ 3. Instale as dependências

```bash
pip install django
```

### ✅ 4. Aplique as migrações do banco de dados

```bash
python manage.py migrate
```

### ✅ 5. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

Abra o navegador e acesse:  
👉 `http://127.0.0.1:8000/`

---

## 🧱 Estrutura do Projeto

```bash
central_precos/
├── app_central_precos/
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   ├── tests.py
│   └── views.py
│
├── central_precos/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── static/
├── db.sqlite3
├── manage.py
└── venv/
```

---

## 📌 Observações

- Certifique-se de que o app `app_central_precos` está registrado no `INSTALLED_APPS` em `settings.py`.
- O projeto usa o banco de dados padrão SQLite para facilitar testes locais.

---

## 📫 Contato

Dúvidas ou sugestões? Entre em contato: gabiel4k12@gmail.com

```

---

Se quiser, posso personalizar esse `README` com seu nome, link real do GitHub, ou até colocar badges e prints do projeto. Só mandar! 🚀
