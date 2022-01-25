import PySimpleGUI as sg


def home():
  layout = [
    [sg.Text('Editor de Texto')],
    [sg.Multiline(key='texto', size=(280, 180))],
    [sg.Input(key='file_name'), sg.Button('Salvar'), sg.Button('Cancelar')]
  ]
  window = sg.Window('EDITOR DE TEXTO', layout, size=(1920, 1080))
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
