import numpy as np

#def 

def step_gd(current_b,current_m,points,lr):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    #Cost function =
    #Lost function =
    #비용함수 == 손실함수
    # 활성화함수 (그래디언트랑 상관없음)

    #연결해놓은 레이어를 임의로 확률적으로 끊으면 성능이 오히려 오른다~~

    for i in range(0,len(points)):
        x = points[i,0] 
        y = points[i,1]
        b_gradient += -(2/N) * ((current_m * x) + current_b) #최소로 만드는!(언덕등반이 최대를 구하는거면 반대!)
        m_gradient += (2/N) * x * (y - ((current_m * x) + current_b))
    new_b = current_b - (lr * b_gradient)
    new_m = current_m - (lr * m_gradient)
    return [new_b,new_m]

def gd(points, st_b, st_m, lr, iter):
    #확률적경사하강법
    b = st_b
    m = st_m
    for i in range(iter):
        b,m = step_gd(b,m,points,lr)
    return [b,m]

if __name__ == "__main__":
    points = np.genfromtxt("./data/data.csv", deletechars=",")
    
    #제일 먼저 런닝메이트
    lerning_rate = 0.001
    init_b = 0 #절편
    init_m = 0 #기울기

    #기본적으로 100번 돌리는거 권장
    num_iter = 1000

    b, m = gd(points, init_b, init_m, lerning_rate, num_iter)
    print(b, m)
    # 알고리즘 만들기
    # 시각화
