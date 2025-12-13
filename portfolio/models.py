from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


def validate_image_size(value):
    filesize = value.size
    if filesize > 5 * 1024 * 1024:
        raise ValidationError("O tamanho maximo da imagem e 5MB")


class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    titulo_profissional = models.CharField(max_length=200)
    resumo = models.TextField()
    foto = models.ImageField(upload_to='perfil/', blank=True, null=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    email = models.EmailField()
    link_cv = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
    
    def __str__(self):
        return self.nome


class Skill(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(
        upload_to='skills/',
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'svg', 'webp']),
            validate_image_size
        ]
    )
    ordem = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'
        ordering = ['ordem']
    
    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    link_repositorio = models.URLField()
    link_deploy = models.URLField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    destaque = models.BooleanField(default=False)
    skills = models.ManyToManyField(Skill, blank=True, related_name='projetos', verbose_name='Habilidades')
    
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-criado_em']
    
    def __str__(self):
        return self.titulo


class ProjetoImagem(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(
        upload_to='projetos/galeria/',
        validators=[
            FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'webp', 'gif']),
            validate_image_size
        ]
    )
    ordem = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Imagem do Projeto'
        verbose_name_plural = 'Imagens do Projeto'
        ordering = ['ordem']
    
    def __str__(self):
        return f"Imagem {self.ordem} - {self.projeto.titulo}"

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    plataforma = models.CharField(max_length=100)
    carga_horaria = models.CharField(max_length=50, blank=True)
    certificado_url = models.URLField(blank=True)
    ano = models.CharField(max_length=4, blank=True)
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['-ano', 'nome']
    
    def __str__(self):
        return f"{self.nome} - {self.plataforma}"


class Certificado(models.Model):
    nome = models.CharField(max_length=200)
    emissor = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='certificados/', blank=True, null=True)
    arquivo_pdf = models.FileField(upload_to='certificados/', blank=True, null=True)
    data_emissao = models.DateField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'
        ordering = ['-data_emissao']
    
    def __str__(self):
        return f"{self.nome} - {self.emissor}"


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Mensagem de Contato'
        verbose_name_plural = 'Mensagens de Contato'
        ordering = ['-criado_em']
    
    def __str__(self):
        return f"{self.nome} - {self.email}"
