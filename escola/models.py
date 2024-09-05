from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=30, blank=False)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    numero_celular = models.CharField(max_length=14)
    
    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    nivel = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado')
    )
    codigo = models.CharField(max_length = 10)
    descricao = models.CharField(max_length=100, blank = False)
    nivel_aluno = models.CharField(max_length = 1, choices = nivel, blank = False, default = 'B')
    
    def __str__(self):
        return self.codigo
    
class Matricula(models.Model):

    periodo = (
        ('M','Matutino'),
        ('V','Vespertino'),
        ('N','Noturno'),
    )
    
    estudante = models.ForeignKey(Estudante, on_delete = models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    periodo = models.CharField(max_length=1, choices=periodo, null=False, blank=False, default='M')

    def __str__(self):
        return f'Curso: {self.curso} | Estudante: {self.estudante}'