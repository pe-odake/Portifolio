from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('projetos/', views.ProjetosView.as_view(), name='projetos'),
    path('contato/', views.ContatoView.as_view(), name='contato'),
    
    path('painel/login/', auth_views.LoginView.as_view(template_name='admin_panel/login.html'), name='login'),
    path('painel/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('painel/', views.DashboardView.as_view(), name='dashboard'),
    
    path('painel/projetos/', views.ProjetoListView.as_view(), name='admin_projetos'),
    path('painel/projetos/novo/', views.ProjetoCreateView.as_view(), name='admin_projeto_criar'),
    path('painel/projetos/<int:pk>/editar/', views.ProjetoUpdateView.as_view(), name='admin_projeto_editar'),
    path('painel/projetos/<int:pk>/excluir/', views.ProjetoDeleteView.as_view(), name='admin_projeto_excluir'),
    path('painel/projetos/imagem/<int:pk>/excluir/', views.ProjetoImagemDeleteView.as_view(), name='admin_projeto_imagem_excluir'),
    
    path('painel/skills/', views.SkillListView.as_view(), name='admin_skills'),
    path('painel/skills/novo/', views.SkillCreateView.as_view(), name='admin_skill_criar'),
    path('painel/skills/<int:pk>/editar/', views.SkillUpdateView.as_view(), name='admin_skill_editar'),
    path('painel/skills/<int:pk>/excluir/', views.SkillDeleteView.as_view(), name='admin_skill_excluir'),
    
    path('painel/cursos/', views.CursoListView.as_view(), name='admin_cursos'),
    path('painel/cursos/novo/', views.CursoCreateView.as_view(), name='admin_curso_criar'),
    path('painel/cursos/<int:pk>/editar/', views.CursoUpdateView.as_view(), name='admin_curso_editar'),
    path('painel/cursos/<int:pk>/excluir/', views.CursoDeleteView.as_view(), name='admin_curso_excluir'),
    
    path('painel/certificados/', views.CertificadoListView.as_view(), name='admin_certificados'),
    path('painel/certificados/novo/', views.CertificadoCreateView.as_view(), name='admin_certificado_criar'),
    path('painel/certificados/<int:pk>/editar/', views.CertificadoUpdateView.as_view(), name='admin_certificado_editar'),
    path('painel/certificados/<int:pk>/excluir/', views.CertificadoDeleteView.as_view(), name='admin_certificado_excluir'),
    
    path('painel/perfil/', views.PerfilUpdateView.as_view(), name='admin_perfil'),
    
    path('painel/mensagens/', views.MensagensListView.as_view(), name='admin_mensagens'),
    path('painel/mensagens/<int:pk>/excluir/', views.MensagemDeleteView.as_view(), name='admin_mensagem_excluir'),
]
