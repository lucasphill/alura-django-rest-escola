from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo.json']

    def test_carregamento_da_fixtures(self):
        '''Teste para verificar carregamento da fixtures'''
        estudante = Estudante.objects.get(cpf='83174917069')
        curso = Curso.objects.get(pk=17)
        self.assertEqual(estudante.numero_celular, '61 95835-7763')
        self.assertEqual(curso.codigo, 'CPOO1')