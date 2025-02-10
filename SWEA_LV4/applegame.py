def get_rotatinon_count(startx,starty,endx,endy,start_direction):
    pass    

    

t_input = int(input())

for t in range(t_input):
    n = int(input())
    arr = [list(map, int, input().split()) for _ in range(n)]
    m = int(input())

    m_positions = []
    for trg_num in range(1,m+1):
        for i, row in enumerate(arr):
            for j, value in enumerate(row):
                if value == trg_num:
                   m_positions.append((i,j))

    rotation_count = 0

    for i in range(m-1):
        if i == 0:
            current_x, current_y = 0, 0
            next_x, next_y = m_positions[0]
        
        else:
            current_x, current_y = m_positions[i]
            next_x, next_y = m_positions[i+1]

        rotation_count += get_rotatinon_count(current_x,current_y,next_x,next_y)