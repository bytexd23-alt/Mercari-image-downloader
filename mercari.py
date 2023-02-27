import requests

item_id = 'm44286225896'  # Replace with the item ID of the Mercari item

for i in range(1, 11):  # Change the range as needed for the number of images
    image_url = f'https://static.mercdn.net/item/detail/orig/photos/{item_id}_{i}.jpg'
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(f'{item_id}_{i}.jpg', 'wb') as f:
            f.write(response.content)
            print(f'Downloaded {item_id}_{i}.jpg')
    else:
        break  # Stop downloading images if the URL returns an error
