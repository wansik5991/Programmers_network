from collections import deque

def solution(n, computers):
    
    check_network = [False for _ in range(n)]
    answer = 0

    def bfs(index) :
        
        queue = deque()
        queue.append(index)
        while queue :
            index = queue.popleft()
            check_network[index] = True

            for i in range(n) :
                if check_network[i] == False and computers[index][i] == 1 :
                    queue.append(i)

    for i in range(n) :
        if check_network[i] == False :
            bfs(i)
            answer += 1
    
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))