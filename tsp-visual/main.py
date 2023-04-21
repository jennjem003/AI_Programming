import pygame
import gfx
import threading
from util import *
from algo_info import ALGO_INFO,DIVIDERS


#0. 알고리즘 껍다구 만들었다 pass
#1 좌표를 찍어야한다.
#2. Loop 를 만들어야 된대..
#
#

def loop():
    for i in range (len(ALGO_INFO)):
        print(ALGO_INFO[i])

    while True:
        gfx.check_events()

        #gfx.draw_text_center(surface,"Hello",font, 50,50)
        gfx.draw_dividers(surface,DIVIDERS)

        for i in range(len(ALGO_INFO)):
            if i < len(sim):
                gfx.draw_text_top_left(surface, ALGO_INFO[i]["name"],
                                       GREEN,
                                       font,
                                       ALGO_INFO[i]["name_coords"])
                gfx.draw_path(surface,list_of_cities_list[i],sim[i].best_order)
            elif len(sim[ALGO_INFO[i]["depends"]].best_order) != 0:
                pass

        pygame.display.update()
        surface.fill(BLACK)

    # 1. 알고리즘 정보를 가져온다.
    # 2. 무한반복
    # 2-1. 알고리즘 배치한다
    # 2-2. 그리면 된다 ==> 어떻게?
    # 그릴거 : 점,선,텍스트
    # draw_point(x,y) => 튜플 => 값 반환하지 않음
    # draw_line(x,y) => 튜플 => 값 반환하지 않음
    # draw_text(x,y) => 대략 객체...?? => 값 반환하지 않음
#==========================================================================#
    #04.20. 15:56
    #1.애니케이션 나오게 하고 싶다 -> 집에 가기 전까지!
    #1. p를 내가 만들어야 됨 (p=간선)(랜덤으로 만들자) -> 답이 있는 랜덤!!(답 없으면 안돌아가~~)=>최고 어렵당^.^
    #1-2. 포팅

pygame.init()
surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), 0, 32)
font = pygame.font.SysFont("Consolas", FONT_HEIGHT)

cities = make_cities(20)
#graph = make_graph_from_city_list(cities)
list_of_cities_list = [ ]
sim = []
threads = []

for i in range(len(ALGO_INFO)):
    list_of_cities_list.append(displace(cities, *ALGO_INFO[i]["displacement"]))


#쓰레드에서 에러(계산이 동기적으로 이뤄지지 않음)
for i in range(len(ALGO_INFO)):
    if ALGO_INFO[i]["depends"] == -1:
        sim.append(ALGO_INFO[i]["sim"](list_of_cities_list))
        threads.append(threading.Thread(target = sim[i].find))
        threads[i].deamon = True


if __name__ == "__main__":

    pygame.display.set_caption("TSP- Visualizer")
    #print(ALGO_INFO)
    #loop()

    #첫번때 시작 위치
    #두번째 시작 위치로 하면 함수 커짐 안됌 algo_inf로 가!