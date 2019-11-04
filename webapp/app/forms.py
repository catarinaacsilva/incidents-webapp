from django import forms
from bootstrap_datepicker_plus import DatePickerInput


STATE = [('a','Em Resolução'),
         ('b','Conclusão'),
         ('c','Encerrada'),
         ('d','Em curso'),
         ('e','Despacho de 1º Alerta')
         ]


DISTRITOS = [('Aveiro','Aveiro'),
             ('Beja', 'Beja'),
             ('Braga', 'Braga'),
             ('Bragança','Bragança'),
             ('Castelo Branco','Castelo Branco'),
             ('Coimbra','Coimbra'),
             ('Évora','Évora'),
             ('Faro','Faro'),
             ('Guarda','Guarda'),
             ('Leiria','Leiria'),
             ('Lisboa','Lisboa'),
             ('Portalegre','Portalegre'),
             ('Porto','Porto'),
             ('Santarém','Santarém'),
             ('Setúbal','Setúbal'),
             ('Viana do Castelo','Viana do Castelo'),
             ('Vila Real','Vila Real'),
             ('Viseu','Viseu')
             ]

NATUREZA=[
    ('a', 'Protecção e Assistência a Pessoas e Bens / Assistência em Saúde / Trauma'),
    ('b', 'Protecção e Assistência a Pessoas e Bens / Assistência em Saúde / Intoxicação'),
    ('c', 'Riscos Tecnológicos / Acidentes / Despiste'),
    ('d', 'Riscos Mistos / Incêndios em Detritos / Detritos confinados'),
    ('e', 'Riscos Tecnológicos / Acidentes / Colisão rodoviária'),
    ('f', 'Riscos Tecnológicos / Incêndios Urbanos ou em Área Urbanizável / Habitacional'),
    ('g', 'Riscos Tecnológicos / Acidentes / Atropelamento rodoviário'),
    ('h', 'Protecção e Assistência a Pessoas e Bens / Intervenção em conflitos legais / Agressão/Violação'),
    ('i', 'Riscos Tecnológicos / Acidentes industriais e tecnológicos / Fuga de Gás em garrafa'),
    ('j', 'Riscos Tecnológicos / Incêndios Urbanos ou em Área Urbanizável / Edifícios degradados ou devolutos'),
    ('k', 'Protecção e Assistência a Pessoas e Bens / Assistência em Saúde / Intoxicação'),
    ('l', 'Protecção e Assistência a Pessoas e Bens / Intervenção em conflitos legais / Suicídio/Homicídio na forma tentada'),
    ('m', 'Riscos Mistos / Comprometimento total ou parcial de segurança, serviços ou estruturas / Inundação de estruturas por água canalizada'),
    ('n', 'Protecção e Assistência a Pessoas e Bens / Assistência e Prevenção a actividades humanas / Limpeza de Via e Sinalização de Perigo'),
    ('o', 'Riscos Mistos / Comprometimento total ou parcial de segurança, serviços ou estruturas / Queda de Árvore'),
    ('p', 'Protecção e Assistência a Pessoas e Bens / Assistência e Prevenção a actividades humanas / Busca e Resgate Terrestre, de Animais'),
    ('q', 'Protecção e Assistência a Pessoas e Bens / Assistência e Prevenção a actividades humanas / Limpeza de Via e Sinalização de Perigo'),
]

class RelatarForm(forms.Form):
    data_ocorrencia = forms.DateField(label='Data da ocorrência', input_formats=['%d-%m-%Y'], widget=DatePickerInput(format='%d-%m-%Y', attrs={'class': 'form-control'}))
    natureza = forms.CharField(label='Natureza', widget=forms.Select(choices=NATUREZA, attrs={'class': 'form-control'}))
    estado = forms.CharField(label='Estado', widget=forms.Select(choices=STATE, attrs={'class': 'form-control'}))
    distrito = forms.CharField(label='Distrito', widget=forms.Select(choices=DISTRITOS, attrs={'class': 'form-control'}))
    concelho = forms.CharField(label='Concelho', widget=forms.TextInput(attrs={'class': 'form-control'}))
    freguesia = forms.CharField(label='Freguesia', widget=forms.TextInput(attrs={'class': 'form-control'}))
    latitude = forms.FloatField(label='Latitude', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    longitude = forms.FloatField(label='Longitude', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    meiosTerrestres = forms.IntegerField(label='Meios Terrestres', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    opTerrestres = forms.IntegerField(label = 'Operacionais Terrestres', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    meiosAereos = forms.IntegerField(label = 'Meios Aéreos', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    opAereos = forms.IntegerField(label = 'Operacionais Aéreos', widget=forms.NumberInput(attrs={'class': 'form-control'}))
