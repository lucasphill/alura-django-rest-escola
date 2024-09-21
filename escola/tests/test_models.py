from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            id = 1,
            nome = 'Teste de Modelo',
            email = 'testedemodelo1@email.com',
            cpf = '95309733060',
            data_nascimento = '2000-01-01',
            numero_celular = '31 99999-9999'
        )

    def test_verifica_atrubutos_de_estudante(self):
        '''Teste que verifica os artibutos do modelo de estudante
        Compara os dados inseridos no banco com os informados abaixo'''
        self.assertEqual(self.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.estudante.email, 'testedemodelo1@email.com')
        self.assertEqual(self.estudante.cpf, '95309733060')
        self.assertEqual(self.estudante.data_nascimento, '2000-01-01')
        self.assertEqual(self.estudante.numero_celular, '31 99999-9999')

class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            id = 1,
            codigo = 'TEST01',
            descricao = 'Teste de Modelo Curso',
            nivel_aluno = 'B'
        )

    def test_verifica_atributos_de_curso(self):
        '''Teste que verifica os artibutos do modelo de curso
        Compara os dados inseridos no banco com os informados abaixo'''
        self.assertEqual(self.curso.codigo, 'TEST01')
        self.assertEqual(self.curso.descricao, 'Teste de Modelo Curso')
        self.assertEqual(self.curso.nivel_aluno, 'B')

class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome = 'Teste de Modelo Matricula',
            email = 'testedemodelo1@email.com',
            cpf = '95309733060',
            data_nascimento = '2000-01-01',
            numero_celular = '31 99999-9999'
        )
        self.curso_matricula = Curso.objects.create(
            codigo = 'TEST01',
            descricao = 'Teste de Modelo Curso',
            nivel_aluno = 'B'
        )
        self.matricula = Matricula.objects.create(
            estudante = self.estudante_matricula,
            curso = self.curso_matricula,
            periodo = 'M'
        )
    
    def test_verifica_atributos_de_matricula(self):
        '''Teste que verifica os artibutos do modelo de curso
        Compara os dados inseridos no banco com os informados abaixo'''
        self.assertEqual(self.matricula.estudante.nome, 'Teste de Modelo Matricula')
        self.assertEqual(self.matricula.curso.codigo, 'TEST01')
        self.assertEqual(self.matricula.periodo, 'M')