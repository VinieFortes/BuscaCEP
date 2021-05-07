import requests
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')


def inicio():
    layout = [
        [sg.Text('Digite o CEP'), sg.Input(key='cep')],
        [sg.Button('BUSCAR')],
        [sg.Text('\nby Vinie')]
    ]
    janela(layout)


def resultado(cep):

    r = requests.get('https://viacep.com.br/ws/'+cep+'/json/')
    resultado = r.json()

    layout = [
        [sg.Text('CEP: '+resultado['cep'])],
        [sg.Text('Logadouro: '+resultado['logradouro'])],
        [sg.Text('Complemento: ' + resultado['complemento'])],
        [sg.Text('Bairro: ' + resultado['bairro'])],
        [sg.Text('localidade: ' + resultado['localidade'])],
        [sg.Text('UF: ' + resultado['uf'])],
        [sg.Text('IBGE: ' + resultado['ibge'])],
        [sg.Text('GIA: ' + resultado['gia'])],
        [sg.Text('DDD: ' + resultado['ddd'])],
        [sg.Text('SIAFI: ' + resultado['siafi'])],
    ]
    janela(layout)


def janela(layout):
    window = sg.Window('Busca CEP', layout)
    while True:
        eventos, valores = window.read()
        if eventos == sg.WIN_CLOSED:
            break
        if eventos == 'BUSCAR':
            passcep = valores['cep']
            resultado(passcep)


inicio()
