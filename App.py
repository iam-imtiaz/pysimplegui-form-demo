
# !/usr/bin/env python
import PySimpleGUI as sg

'''
    Example of Form GUI
'''

def main():
    sg.theme('DarkAmber')
    first_column_layout = [
        [sg.Text('First Name'),
        sg.InputText('', key='in1', size=(20, 1))],
        [sg.Text('Last Name'),
         sg.InputText('', key='in2', size=(20, 1))],
        [sg.Text('Nationality'),
         sg.InputText('', key='in3', size=(20, 1))]]

    second_column_layout = [
        [sg.Text('Date of Birth'), sg.InputText(key='Date', size=(10, 1)),
         sg.CalendarButton("Select Date", close_when_date_chosen=True, target="Date", format='%d/%m/%y', size=(10, 1))],
        [sg.T("Time:"), sg.InputText(size=(3, 1), default_text='hh'), sg.InputText('mm', size=(3, 1)), sg.InputText('AM',size=(3, 1))],
        [sg.Text('Gender'),
        sg.Radio('Male', "RADIO1", default=False),
        sg.Radio('Female', "RADIO1", default=False)]
    ]

    third_layout_column = [
        [sg.Text('Resume', size=(15, 1), justification='right'),
         sg.InputText('Default Folder', key='folder'), sg.FolderBrowse()],
        [sg.Button('Submit')]
    ]

    layout = [
        [sg.Column(first_column_layout,element_justification='center'),
         sg.VSeperator(),
         sg.Column(second_column_layout)],
        [sg.Text('_' * 80)],
        [sg.Column(third_layout_column, element_justification='center')],
    ]

    window = sg.Window('Form Fill Demonstration', layout, default_element_size=(40, 1), grab_anywhere=False)

    while True:
        event, values = window.read()
        if event in ('Exit', None):
            break

    window.close()


if __name__ == '__main__':
    main()

