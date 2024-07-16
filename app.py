import PySimpleGUI as sg

def calc(peso, altura):
    imc = peso / (altura * altura)
    return imc

def situacao_peso(imc):
    if imc < 17:
        return 'Muito abaixo do peso 😔', 'white', 'black'
    elif 17 <= imc < 18.5:
        return 'Abaixo do peso 😕', 'gray', 'black'
    elif 18.5 <= imc < 25:
        return 'Peso normal 😊', 'green', 'white'
    elif 25 <= imc < 30:
        return 'Acima do peso 😐', 'yellow', 'black'
    elif 30 <= imc < 35:
        return 'Obesidade I 😟', 'orange', 'black'
    elif 35 <= imc < 40:
        return 'Obesidade II (Severa) 😧', 'red', 'white'
    else:
        return 'Obesidade III (Mórbida) ☠', 'black', 'white'

def interface():
    sg.theme('Dark Purple 6')

    layout = [
        [sg.Text('Digite seu peso (kg)')],
        [sg.Input(key='peso')],
        [sg.Text('Digite sua altura (m)')],
        [sg.Input(key='altura')],
        [sg.Button(button_text='Calcular IMC')],
        [sg.Text(key='imc', size=(20, 1), font=('Helvetica', 12, 'bold'))],
        [sg.Text(key='situacao', size=(25, 1), font=('Helvetica', 12, 'bold'))]
    ]
    window = sg.Window('Calculadora de IMC', layout=layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == 'Calcular IMC':
            try:
                peso = float(values['peso'])
                altura = float(values['altura'])
                if peso <= 0 or altura <= 0:
                    sg.popup('Peso e altura devem ser valores positivos.', title='Erro')
                    continue
                
                imc = calc(peso, altura)
                situacao, background_color, text_color = situacao_peso(imc)
                
                window['imc'].update(f'Seu IMC é de {imc:.2f}', text_color=text_color, background_color=background_color)
                window['situacao'].update(situacao, text_color=text_color, background_color=background_color)
            except ValueError:
                sg.popup('Por favor, insira valores numéricos válidos.', title='Erro')
    window.close()

interface()
