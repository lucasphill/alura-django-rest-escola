from django.test import TestCase
from escola.models import Estudante, Curso, Matricula
from escola.serializer import EstudanteSerializer, CursoSerializer, MatriculaSerializer

class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            id = 1,
            nome = 'Teste de Modelo',
            email = 'testedemodelo1@email.com',
            cpf = '95309733060',
            data_nascimento = '2000-01-01',
            numero_celular = '31 99999-9999'
        )
        self.serializer_estudante = EstudanteSerializer(instance=self.estudante)

    def test_verifica_campos_serializados_de_estudante(self):
        '''Teste que verifica os campos serializados de estudante
        Compara as chaves serializadas com os informados abaixo'''
        dados = self.serializer_estudante.data
        self.assertEqual(set(dados.keys()), set(['id', 'nome', 'email', 'cpf', 'data_nascimento', 'numero_celular']))

    def test_verifica_conteudo_dos_campos_serializados_de_estudante(self):
        '''Teste que verifica o conteudo dos campos serializados de estudante
        Compara o conteudo serializado com os informados abaixo'''
        dados = self.serializer_estudante.data
        self.assertEqual(dados['nome'], self.estudante.nome)
        self.assertEqual(dados['email'], self.estudante.email)
        self.assertEqual(dados['cpf'], self.estudante.cpf)
        self.assertEqual(dados['data_nascimento'], self.estudante.data_nascimento)
        self.assertEqual(dados['numero_celular'], self.estudante.numero_celular)

class SerializerCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso(
            id = 1,
            codigo = 'TEST01',
            descricao = 'Teste de Modelo Curso',
            nivel_aluno = 'B'
        )
        self.serializer_curso = CursoSerializer(instance=self.curso)

    def test_verifica_campos_serializados_de_curso(self):
        '''Teste que verifica os campos serializados de curso
        Compara as chaves serializadas com os informados abaixo'''
        dados = self.serializer_curso.data
        self.assertEqual(set(dados.keys()), set(['id','codigo', 'descricao', 'nivel_aluno']))

    def test_verifica_conteudo_dos_campos_serializados_de_curso(self):
        '''Teste que verifica o conteudo dos campos serializados de cruso
        Compara o conteudo serializado com os informados abaixo'''
        dados = self.serializer_curso.data
        self.assertEqual(dados['codigo'], self.curso.codigo)
        self.assertEqual(dados['descricao'], self.curso.descricao)
        self.assertEqual(dados['nivel_aluno'], self.curso.nivel_aluno)

class SerializerMatriculaTestCase(TestCase):
    # def teste_mostra_matricula(self):
    #     dados = self.serializer_matricula.data
    #     self.fail(dados)

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
        self.serializer_matricula = MatriculaSerializer(instance=self.matricula)
        
    def test_verifica_campos_serializados_de_matricula(self):
        '''Teste que verifica os campos serializados de matricula
        Compara as chaves serializadas com os informados abaixo'''
        dados = self.serializer_matricula.data
        self.assertEqual(set(dados.keys()), set(['id','estudante','curso','periodo']))

    def test_verifica_conteudo_dos_campos_serializados_de_matricula(self):
        '''Teste que verifica o conteudo dos campos serializados de matricula
        Compara o conteudo serializado com os informados abaixo'''
        dados = self.serializer_matricula.data
        self.assertEqual(dados['estudante'], self.matricula.estudante.id)
        self.assertEqual(dados['curso'], self.matricula.curso.id)
        self.assertEqual(dados['periodo'], self.matricula.periodo)