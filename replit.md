# Portfolio Django

## Overview
Portfolio profissional completo desenvolvido em Django com tema escuro moderno. Inclui area publica para exibicao do portfolio e painel administrativo personalizado para gestao de conteudo.

## Recent Changes
- 2024-12-10: Projeto inicial criado com Django 5.2
- 2024-12-10: Models criados (Projeto, Skill, Curso, Certificado, Perfil, Contato)
- 2024-12-10: Painel administrativo personalizado com CRUD completo
- 2024-12-10: Area publica com design responsivo tema escuro
- 2024-12-10: Sistema de autenticacao configurado

## User Preferences
- Design: Tema escuro (#1F2937, #111827, #3A86FF)
- Framework CSS: Bootstrap 5
- Fonte: Inter
- Idioma: Portugues Brasileiro

## Project Architecture

### Estrutura de Pastas
```
portfolio/
  models.py       # Modelos: Projeto, Skill, Curso, Certificado, Perfil, Contato
  views.py        # Views com Class-Based Views
  urls.py         # Rotas da aplicacao
  forms.py        # Formularios Django
  templates/
    portfolio/    # Templates da area publica
    admin_panel/  # Templates do painel administrativo
  static/
    portfolio/
      css/        # style.css (publico), admin.css (painel)
      js/         # main.js
      img/        # Imagens estaticas
media/            # Uploads de usuarios (projetos, certificados, perfil)
```

### URLs Principais
- `/` - Pagina inicial do portfolio
- `/projetos/` - Lista de todos os projetos
- `/contato/` - Formulario de contato
- `/painel/` - Dashboard administrativo (requer login)
- `/painel/login/` - Login do painel

### Credenciais de Acesso
- Usuario: admin
- Senha: admin123

### Banco de Dados
- SQLite (db.sqlite3)

### Comandos Uteis
```bash
python manage.py runserver 0.0.0.0:5000  # Iniciar servidor
python manage.py makemigrations          # Criar migracoes
python manage.py migrate                 # Aplicar migracoes
python manage.py createsuperuser         # Criar admin
```
