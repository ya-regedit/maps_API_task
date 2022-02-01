from requests import get
import sys

import pygame
import io

response = None


def get_address_coords(address):
    global response
    addres = address
    apikey = '40d1649f-0493-4b70-98ba-98533de7710b'
    request_url = f"http://geocode-maps.yandex.ru/1.x/?apikey={apikey}&geocode={addres}&format=json"
    response = get(request_url)
    jsonn = response.json()
    lon, lat = jsonn['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
    return lon, lat


def get_map(coords):
    lon, lat = coords
    global response
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={lon},{lat}&spn=100,20&l=sat,skl"
    response = get(map_request)
    return io.BytesIO(response.content)


map_file = get_map(get_address_coords('Австралия'))

if not response:
    print("Ошибка выполнения запроса")
    sys.exit(1)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
