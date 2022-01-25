import PySimpleGUI as sg


def home():
  sg.theme('darkgreen2')
  layout = [
    [sg.Text('Editor')],
    [sg.Multiline(key='texto', size=(60, 27))],
    [sg.Input(key='file_name'), sg.Button('Salvar'), sg.Button('Cancelar')]
  ]
  window = sg.Window('EDITOR DE TEXTO', layout, resizable=True)
  while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
      break
    elif event == 'Salvar':
      name = values['file_name']
      texto = values['texto']
      arq = open(name, 'x')
      arq.write(texto)
      arq.close()
      sg.Text(f'{name}, criado com sucesso!')
  window.close()

if __name__ == '__main__':
    home()