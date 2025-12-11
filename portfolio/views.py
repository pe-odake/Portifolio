from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Projeto, Skill, Curso, Certificado, Perfil, Contato
from .forms import ProjetoForm, SkillForm, CursoForm, CertificadoForm, PerfilForm, ContatoForm


class HomeView(TemplateView):
    template_name = 'portfolio/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfil'] = Perfil.objects.first()
        context['projetos'] = Projeto.objects.all()[:6]
        context['projetos_destaque'] = Projeto.objects.filter(destaque=True)[:4]
        context['skills'] = Skill.objects.all()
        context['cursos'] = Curso.objects.all()
        context['certificados'] = Certificado.objects.all()
        return context


class ProjetosView(ListView):
    model = Projeto
    template_name = 'portfolio/projetos.html'
    context_object_name = 'projetos'


class ContatoView(FormView):
    template_name = 'portfolio/contato.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato')
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Mensagem enviada com sucesso!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfil'] = Perfil.objects.first()
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_panel/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_projetos'] = Projeto.objects.count()
        context['total_skills'] = Skill.objects.count()
        context['total_cursos'] = Curso.objects.count()
        context['total_certificados'] = Certificado.objects.count()
        context['total_mensagens'] = Contato.objects.filter(lido=False).count()
        context['projetos_recentes'] = Projeto.objects.all()[:5]
        context['mensagens_recentes'] = Contato.objects.filter(lido=False)[:5]
        return context


class ProjetoListView(LoginRequiredMixin, ListView):
    model = Projeto
    template_name = 'admin_panel/projetos_list.html'
    context_object_name = 'projetos'


class ProjetoCreateView(LoginRequiredMixin, CreateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = 'admin_panel/form.html'
    success_url = reverse_lazy('admin_projetos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Novo Projeto'
        context['voltar_url'] = 'admin_projetos'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Projeto criado com sucesso!')
        return super().form_valid(form)


class ProjetoUpdateView(LoginRequiredMixin, UpdateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = 'admin_panel/form.html'
    success_url = reverse_lazy('admin_projetos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Projeto'
        context['voltar_url'] = 'admin_projetos'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Projeto atualizado com sucesso!')
        return super().form_valid(form)


class ProjetoDeleteView(LoginRequiredMixin, DeleteView):
    model = Projeto
    template_name = 'admin_panel/confirm_delete.html'
    success_url = reverse_lazy('admin_projetos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Projeto'
        context['voltar_url'] = 'admin_projetos'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Projeto excluido com sucesso!')
        return super().form_valid(form)


class SkillListView(LoginRequiredMixin, ListView):
    model = Skill
    template_name = 'admin_panel/skills_list.html'
    context_object_name = 'skills'


class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'admin_panel/form.html'
    success_url = reverse_lazy('admin_skills')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nova Habilidade'
        context['voltar_url'] = 'admin_skills'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Habilidade criada com sucesso!')
        return super().form_valid(form)


class SkillUpdateView(LoginRequiredMixin, UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = 'admin_panel/form.html'
    success_url = reverse_lazy('admin_skills')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Habilidade'
        context['voltar_url'] = 'admin_skills'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Habilidade atualizada com sucesso!')
        return super().form_valid(form)


class SkillDeleteView(LoginRequiredMixin, DeleteView):
    model = Skill
    template_name = 'admin_panel/confirm_delete.html'
    success_url = reverse_lazy('admin_skills')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Habilidade'
        context['voltar_url'] = 'admin_skills'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Habilidade excluida com sucesso!')
        return super().form_valid(form)


class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'admin_panel/cursos_list.html'
    context_object_name = 'cursos'


class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'admin_panel/form.html'
    success_url = reverse_lazy('admin_cursos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Novo Curso'
        context['voltar_url'] = 'admin_cursos'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Curso criado com sucesso!')
        return super().form_valid(form)


class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'admin_panel/form.html'
    success_url = reverse_lazy('admin_cursos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Curso'
        context['voltar_url'] = 'admin_cursos'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Curso atualizado com sucesso!')
        return super().form_valid(form)


class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = 'admin_panel/confirm_delete.html'
    success_url = reverse_lazy('admin_cursos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Curso'
        context['voltar_url'] = 'admin_cursos'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Curso excluido com sucesso!')
        return super().form_valid(form)


class CertificadoListView(LoginRequiredMixin, ListView):
    model = Certificado
    template_name = 'admin_panel/certificados_list.html'
    context_object_name = 'certificados'


class CertificadoCreateView(LoginRequiredMixin, CreateView):
    model = Certificado
    form_class = CertificadoForm
    template_name = 'admin_panel/form.html'
    success_url = reverse_lazy('admin_certificados')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Novo Certificado'
        context['voltar_url'] = 'admin_certificados'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Certificado criado com sucesso!')
        return super().form_valid(form)


class CertificadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Certificado
    form_class = CertificadoForm
    template_name = 'admin_panel/form.html'
    success_url = reverse_lazy('admin_certificados')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Certificado'
        context['voltar_url'] = 'admin_certificados'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Certificado atualizado com sucesso!')
        return super().form_valid(form)


class CertificadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Certificado
    template_name = 'admin_panel/confirm_delete.html'
    success_url = reverse_lazy('admin_certificados')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Certificado'
        context['voltar_url'] = 'admin_certificados'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Certificado excluido com sucesso!')
        return super().form_valid(form)


class PerfilUpdateView(LoginRequiredMixin, UpdateView):
    model = Perfil
    form_class = PerfilForm
    template_name = 'admin_panel/perfil_form.html'
    success_url = reverse_lazy('admin_perfil')
    
    def get_object(self, queryset=None):
        obj, created = Perfil.objects.get_or_create(pk=1, defaults={
            'nome': 'Seu Nome',
            'titulo_profissional': 'Desenvolvedor Full-Stack',
            'resumo': 'Sobre voce...',
            'email': 'seu@email.com'
        })
        return obj
    
    def form_valid(self, form):
        messages.success(self.request, 'Perfil atualizado com sucesso!')
        return super().form_valid(form)


class MensagensListView(LoginRequiredMixin, ListView):
    model = Contato
    template_name = 'admin_panel/mensagens_list.html'
    context_object_name = 'mensagens'
    
    def get_queryset(self):
        Contato.objects.filter(lido=False).update(lido=True)
        return Contato.objects.all()


class MensagemDeleteView(LoginRequiredMixin, DeleteView):
    model = Contato
    template_name = 'admin_panel/confirm_delete.html'
    success_url = reverse_lazy('admin_mensagens')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Mensagem'
        context['voltar_url'] = 'admin_mensagens'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Mensagem excluida com sucesso!')
        return super().form_valid(form)
