import PySimpleGUI as sg

# calcular o imc
def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi

# Analisa o valor do IMC e define a categoria correspondente com as cores associadas
def analyze_bmi_and_define_category_color(bmi):
    if bmi < 17:
        return 'Very underweight 😔', 'white', 'black'
    elif 17 <= bmi < 18.5:
        return 'Underweight 😕', 'gray', 'black'
    elif 18.5 <= bmi < 25:
        return 'Normal weight 😊', 'green', 'white'
    elif 25 <= bmi < 30:
        return 'Overweight 😐', 'yellow', 'black'
    elif 30 <= bmi < 35:
        return 'Obesity I 😟', 'orange', 'black'
    elif 35 <= bmi < 40:
        return 'Obesity II (Severe) 😧', 'red', 'white'
    else:
        return 'Obesity III (Morbid) ☠', 'black', 'white'

# Cria a interface gráfica para calcular e exibir o IMC e a categoria de peso
def interface():
    sg.theme('Dark Purple 6')

    layout = [
        [sg.Text('Enter your weight (kg)')],
        [sg.Input(key='weight')],
        [sg.Text('Enter your height (m)')],
        [sg.Input(key='height')],
        [sg.Button(button_text='Calculate BMI')],
        [sg.Text(key='bmi', size=(20, 1), font=('Helvetica', 12, 'bold'))],
        [sg.Text(key='category', size=(25, 1), font=('Helvetica', 12, 'bold'))]
    ]
    # Cria a janela com o layout definido
    window = sg.Window('BMI Calculator', layout=layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == 'Calculate BMI':
            try:
                weight = float(values['weight'])
                height = float(values['height'])
                if weight <= 0 or height <= 0:
                    sg.popup('Weight and height must be positive values.', title='Error')
                    continue

                # Calcula o IMC e obtém a categoria e as cores
                bmi = calculate_bmi(weight, height)
                category, background_color, text_color = analyze_bmi_and_define_category_color(bmi)
                
                # Atualiza os textos na interface com o IMC e a categoria
                window['bmi'].update(f'Your BMI is {bmi:.2f}', text_color=text_color, background_color=background_color)
                window['category'].update(category, text_color=text_color, background_color=background_color)
            except ValueError:
                sg.popup('Please enter valid numeric values.', title='Error')
    window.close()

interface()
