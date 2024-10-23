from datetime import date
from django import forms
from reserva.models import Reserva

class ReservaForm(forms.ModelForm):
    
    def clean_data(self):
        data = self.cleaned_data['data']
        hoje = date.today()
        if data < hoje:
            raise forms.ValidationError('Não é possivel realizar uma reserva para o passado!')
        reservas_manha = Reserva.objects.filter(data=data).count()
        reservas_tarde = Reserva.objects.filter(data=data).count()
        if reservas_manha or reservas_tarde >= 4:
            raise forms.ValidationError('Limite de 4 reservas por dia atingido. Escolha outra data!')
        return data
    
    class Meta:
        model = Reserva
        fields = [
            'nome', 'email', 'nome_pet', 'data', 'turno',
            'tamanho', 'observacoes'
        ]
        