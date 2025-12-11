from django import forms
from .models import Projeto, Skill, Curso, Certificado, Perfil, Contato


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'imagem', 'link_repositorio', 'link_deploy', 'destaque']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo do projeto'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descricao detalhada do projeto'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'link_repositorio': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/...'}),
            'link_deploy': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'destaque': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['nome', 'imagem', 'ordem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da habilidade'}),
            'ordem': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
        }


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'plataforma', 'carga_horaria', 'certificado_url', 'ano']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do curso'}),
            'plataforma': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Udemy, Coursera'}),
            'carga_horaria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 40h'}),
            'certificado_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link do certificado'}),
            'ano': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2024'}),
        }


class CertificadoForm(forms.ModelForm):
    class Meta:
        model = Certificado
        fields = ['nome', 'emissor', 'imagem', 'arquivo_pdf', 'data_emissao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do certificado'}),
            'emissor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Google, Microsoft'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'arquivo_pdf': forms.FileInput(attrs={'class': 'form-control'}),
            'data_emissao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nome', 'titulo_profissional', 'resumo', 'foto', 'github', 'linkedin', 'email', 'link_cv', 'instagram']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome completo'}),
            'titulo_profissional': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Desenvolvedor Full-Stack'}),
            'resumo': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Fale sobre voce...'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'github': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/...'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://linkedin.com/in/...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'}),
            'link_cv': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link para seu CV'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://instagram.com/...'}),
        }


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu.email@exemplo.com'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Deixe sua mensagem aqui...'}),
        }
