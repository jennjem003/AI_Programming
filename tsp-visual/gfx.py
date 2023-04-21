import pygame
import sys
from pygame.locals import *
from util import *

# 프로그램이 종료된다는게 os는 어떻게 알고있는가?
# int main()
#{
#    return 0 
# }


def check_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def draw_text_center(surface, text, font, x, y):
    text_obj = font.render(text, 1, RED)
    text_rect = text_obj.get_rect()
    text_rect.center = (x,y)
    surface.blit(text_obj,text_rect)

def draw_text_top_left(surface, text, color,font, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x,y)
    surface.blit(text_obj,text_rect)

def draw_dividers(surface, DIVIDERS):
    for x1,y1,x2,y2 in DIVIDERS:
        pygame.draw.aaline(surface,WHITE,(x1,y1),(x2,y2))

def make_graph_from_city_list(cities):
    n = len(cities)
    graph = [[0 for i in range(n)] for j in range(n)] #-> for함수 두번 한번에 돌리는거
    #뒤에서부터 읽어 => 
    for i in range(n):
        city_a = cities[i]
        for j in range(i,n):
            if i == j:
                graph[i][j] = 0
            else:
                city_b = cities[j]

                d = (city_a - city_b).length()
                graph[i][j] = graph[j][i] = d #할당연산자만 뒤에서 읽는다!
  
        return graph
    # 2개 => for 2개
    # for i in range (n):
    #   for j on range(n):
    #       [i,j]

def draw_path(surface, cities, order):
    if (len(order) != len(cities)):
        return
    r = CITY_SIZE // len(cities)
    r = int(max(MIN_CITY_SIZE,r))
    r = int(min(MAX_CITY_SIZE,r))
    order = order[order.index(0):] + order[:order.index(0)]
    for i in range(len(order)):
        city_a = cities[order[i % len(order)]]
        city_b = cities[order(i+1) % len(order)]
        if i == 0:
            pygame.draw.circle(surface, BLUE, (int(city_a.x),int(city_a.y),r))
    
        else:
            pygame.draw.circle(surface, RED, (int(city_a.x),int(city_a.y),r))
        pygame.draw.aaline(surface, WHITE, city_a, city_b, 2)
