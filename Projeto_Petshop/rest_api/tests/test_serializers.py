import pytest
import datetime
from model_bakery import baker
from reserva.models import Petshop
from rest_api.serializers import AgendamentoModelSerializer

from reserva.models import Petshop


@pytest.fixture
def dados_agendamento_errado():
    ontem = datetime.date.today() - datetime.timedelta(days=1)
    petshop = baker.make(Petshop)
    return {
        'nome': 'nome teste', 'email': 'email@email.com',
        'nome_pet': 'pet teste', 'data': ontem, 'turno': 'manhã',
        'tamanho': 0, 'obsercacoes': '', 'petshop': petshop.pk,
    }
    
@pytest.mark.django_db
def test_data_agendamento_invalido(dados_agendamento_errado):
    serializer = AgendamentoModelSerializer(data=dados_agendamento_errado)
    assert not serializer.is_valid()
    