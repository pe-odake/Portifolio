from django import forms
from django.core.validators import FileExtensionValidator
from .models import Projeto, Skill, Curso, Certificado, Perfil, Contato, ProjetoImagem


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class ProjetoForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'skills-checkbox-list'}),
        required=False,
        label='Habilidades'
    )
    
    galeria = MultipleFileField(
        required=False,
        label='Imagens da Galeria',
        widget=MultipleFileInput(attrs={
            'class': 'form-control',
            'accept': 'image/png,image/jpeg,image/webp,image/gif'
        })
    )

    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'imagem', 'link_repositorio', 'link_deploy', 'destaque', 'skills']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo do projeto'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descricao detalhada do projeto'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'link_repositorio': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/...'}),
            'link_deploy': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'destaque': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_galeria(self):
        files = self.files.getlist('galeria')
        allowed_extensions = ['png', 'jpg', 'jpeg', 'webp', 'gif']
        max_size = 5 * 1024 * 1024
        
        for file in files:
            ext = file.name.split('.')[-1].lower()
            if ext not in allowed_extensions:
                raise forms.ValidationError(f"Formato de imagem nao suportado: {ext}")
            if file.size > max_size:
                raise forms.ValidationError(f"Imagem {file.name} excede o tamanho maximo de 5MB")
        
        return files


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['nome', 'imagem', 'ordem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da habilidade'}),
            'imagem': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/png,image/jpeg,image/svg+xml,image/webp'
            }),
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
