from django.db import models


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


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    link_repositorio = models.URLField()
    link_deploy = models.URLField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    destaque = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-criado_em']
    
    def __str__(self):
        return self.titulo


class Skill(models.Model):
    
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='skills/', blank=True, null=True)
    ordem = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'
        ordering = ['ordem']
    
    def __str__(self):
        return f"{self.nome} - {self.categoria}"

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
