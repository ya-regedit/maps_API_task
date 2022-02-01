from requests import get
import sys

import pygame
import io

SIZE = (600, 400)


class Map:
    def __init__(self, coords, spn=(100,20), l='map'):
        self.l = l
        self.spn = spn
        self.coords = coords
        self.cur_map = self.get_map()

    def get_map(self):
        lon, lat = self.coords
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={lon},{lat}&spn={self.spn[0]},{self.spn[1]}&l={self.l}"
        print(map_request)
        self.response = get(map_request)
        if not self.response:
            print("Ошибка выполнения запроса")
            sys.exit(1)
        return self.response.content

    def update(self, coords=None, spn=None, l=None):
        flag = False
        if coords is not None:
            self.coords = coords
            flag = True
        if spn is not None:
            self.spn = spn
            flag = True
        if l is not None:
            self.l = l
            flag = True
        if flag:
            self.cur_map = self.get_map()


def get_address_coords(address):
    global response
    addres = address
    apikey = '40d1649f-0493-4b70-98ba-98533de7710b'
    request_url = f"http://geocode-maps.yandex.ru/1.x/?apikey={apikey}&geocode={addres}&format=json"
    response = get(request_url)
    jsonn = response.json()
    lon, lat = jsonn['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
    return lon, lat


pygame.init()
screen = pygame.display.set_mode(SIZE)
coords = 37.6, 55.7
spn = 10, 2
l = 'map'
mainMap = Map(coords, spn, l)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(pygame.image.load(io.BytesIO(mainMap.cur_map)), (0, 0))
    pygame.display.flip()
