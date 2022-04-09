from django.db import models
from django.contrib.auth.models import User


class Referencias(models.Model):
    arquivo = models.FileField(upload_to='Referencias')

    def __str__(self) -> str:
        return self.arquivo.url

class Jobs(models.Model):
    categoria_choices = (('D', 'Design'),
                         ('EV', 'Edição de Vídeo'),
                         ('MD', 'Marketing Digital'),
                         ('LP', 'Landing Page'))

    status_choices = (('C', 'Em criação'),
                      ('AA', 'Aguardando aprovação'),
                      ('F', 'Finalizado'))


    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.CharField(max_length=4, choices=categoria_choices, default="D")
    prazo_entrega = models.DateTimeField()
    preco = models.FloatField()
    referencias = models.ManyToManyField(Referencias)
    profissional = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    reservado = models.BooleanField(default=False)
    status = models.CharField(max_length=4, default="AA")

    def __str__(self) -> str:
        return self.titulo
    
