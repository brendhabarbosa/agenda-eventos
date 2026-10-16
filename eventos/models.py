from django.db import models

# Create your models here.

class Local(models.Model):
    nome = models.CharField(max_length=250, unique=True)
    endereco = models.CharField(max_length=250)
    capacidade = models.PositiveIntegerField()
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locais'

class Categoria(models.Model):
    nome = models.CharField(max_length=250, unique=True)
    def __str__(self):
        return self.nome
    class Meta: 
        ordering = ["nome"]
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Evento(models.Model):
    titulo = models.CharField(max_length=250)
    descricao = models.TextField()
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    criado_em = models.DateField(auto_now_add=True)
    local = models.ForeignKey(Local, on_delete=models.PROTECT, null=False, related_name="eventos")
    categoria = models.ManyToManyField(Categoria, null=True, blank=True, related_name="eventos")
    class Meta:
        ordering = ["inicio"]
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    def __str__(self):
        return self.titulo
    def vagas_restantes(self):
        return self.local.capacidade - self.inscricoes.count()

class Atividade(models.Model):
    titulo = models.CharField(max_length=250)
    palestrante = models.CharField(max_length=250)
    horario = models.TimeField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null= False, related_name="atividades")

    def __str__(self):
        return self.titulo
    class Meta:
        ordering = ["horario"]
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

class Inscricao(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField()
    inscrito_em = models.DateTimeField(auto_now_add=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="inscricoes")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

class Relatorio(models.Model):
    presentes = models.PositiveIntegerField()
    observacoes = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.presentes
    class Meta: 
        verbose_name = 'Relatório'
        verbose_name_plural = 'Relatórios'