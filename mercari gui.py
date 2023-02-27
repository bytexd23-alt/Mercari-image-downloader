import os
import requests
import PySimpleGUI as sg

# Set up PySimpleGUI theme
sg.theme('DarkBlue')

# Define GUI layout
layout = [
    [sg.Text('Mercari Image Downloader', font=('Segoe UI', 14, 'bold'))],
    [sg.Text('Item ID or URL:'), sg.InputText('', key='item_id', size=(40, 1))],
    [sg.Text('Save Location:'), sg.InputText('', key='save_loc', size=(40, 1)), sg.FolderBrowse('Browse')],
    [sg.Button('Download Images'), sg.Button('Exit')],
]

# Define window and run event loop
window = sg.Window('Mercari Image Downloader', layout, resizable=True, element_justification='c', alpha_channel=0.9, grab_anywhere=True, border_depth=0, no_titlebar=True, keep_on_top=True, use_custom_titlebar=True, enable_close_attempted_event=True, finalize=True)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit':
        break

    elif event == 'Download Images':
        item_id = values['item_id'].split('m')[-1]
        save_loc = values['save_loc']

        if not item_id or not save_loc:
            sg.popup('Please enter item ID/URL and select save location.', title='Error', icon='error')
            continue

        # Create folder with item ID
        folder_path = os.path.join(save_loc, f'm{item_id}')
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Download images
        for i in range(1, 11):
            image_url = f'https://static.mercdn.net/item/detail/orig/photos/m{item_id}_{i}.jpg'
            response = requests.get(image_url)
            if response.status_code == 200:
                with open(os.path.join(folder_path, f'm{item_id}_{i}.jpg'), 'wb') as f:
                    f.write(response.content)
                    print(f'Downloaded m{item_id}_{i}.jpg')
            else:
                break

        sg.popup(f'Images downloaded to {folder_path}.', title='Success', icon='info')

window.close()
