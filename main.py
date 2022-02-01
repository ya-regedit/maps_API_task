from requests import get
import sys

import pygame
import io

SIZE = (600, 400)


class Map:
    def __init__(self, coords, l='map', scale=1):
        self.l = l
        self.coords = coords
        self.scale = scale
        self.cur_map = self.get_map()

    def get_map(self):
        lon, lat = self.coords
        map_request = f"""http://static-maps.yandex.ru/1.x/?ll={lon},{lat}&l={self.l}&z={self.scale}"""
        print(map_request)
        self.response = get(map_request)
        if not self.response:
            print("Ошибка выполнения запроса")
            sys.exit(1)
        return self.response.content

    def update(self, coords=None, l=None, scale=None):
        flag = False
        if coords is not None:
            self.coords = coords
            flag = True
        if scale is not None:
            self.scale = scale
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
scale = 1
l = 'map'
mainMap = Map(coords, l, scale)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_PAGEUP:
            mainMap.update(scale=max(0, mainMap.scale + 1))
            print(mainMap.scale)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_PAGEDOWN:
            mainMap.update(scale=min(21, mainMap.scale - 1))
            print(mainMap.scale)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            c = mainMap.coords[0] - 20 / 2 ** mainMap.scale, mainMap.coords[1]
            if c[0] > 180:
                c = -180, c[1]
            mainMap.update(coords=c)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            c = mainMap.coords[0] - 20 / 2 ** mainMap.scale, mainMap.coords[1]
            if c[0] < 180:
                c = 180, c[1]
            mainMap.update(coords=c)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            c = mainMap.coords[0], mainMap.coords[1] + 20 / 2 ** mainMap.scale
            if c[1] > 89:
                c = c[0], 89
            mainMap.update(coords=c)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            c = mainMap.coords[0], mainMap.coords[1] - 20 / 2 ** mainMap.scale
            if c[1] < -89:
                c = c[0], -89
            mainMap.update(coords=c)
    screen.blit(pygame.image.load(io.BytesIO(mainMap.cur_map)), (0, 0))
    pygame.display.flip()
