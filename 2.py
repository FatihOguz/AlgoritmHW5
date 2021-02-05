nV = 10
INF = 999

def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)

def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = [    [2,5,4,INF,INF,INF,INF,INF,INF,INF],
         [INF,5,INF,1,4,INF,INF,INF,INF,INF],
         [INF,INF,4,INF,4,7,INF,INF,INF,INF],
         [INF, INF, INF, 1,INF,INF,8,6,INF,INF],
         [INF, INF, INF, INF,4,INF,INF,6,9,INF],
         [INF, INF, INF, INF,INF,7,INF,INF,9,6],
         [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF],
         [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF],
         [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF],
         [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF]]
print("a  b  c  d  e  f   g   h   i   j")
floyd_warshall(G)
