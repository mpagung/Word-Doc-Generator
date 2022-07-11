import PySimpleGUI as sg

from datetime import date
today=date.today()
today=today.timetuple()
today=tuple([today[1],today[0],today[2]]) #convert to tuple format from sg.popup_get_date

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
product_layout = [  [sg.Text('Produk')],
            [sg.Listbox(values=['Minyak','Kaca','Hawk'], size=(30,6))],
            [sg.Checkbox("Pilih hari:", default=False, key="-IN-")],
            [sg.Text('Contract #'), sg.InputText()],
            [sg.Text('Shipping marks'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Shipping list info', product_layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif values["-IN-"] == True:
        current_date=sg.popup_get_date()
    else:
        current_date=today#.strftime("(%m, %d, %Y)")
    print('You entered ', values[0], values[1], values[2], current_date, type(current_date))

window.close()   