def get_neighbors(i, n):
    left = (i - 1) % n
    right = (i + 1) % n
    return left, right

def get_cyclic_order(pts, n):
    pts_sorted = sorted(pts)
    
    max_gap = -1
    start_index = 0  
    for i in range(len(pts_sorted)):
        next_i = (i + 1) % len(pts_sorted)
        if pts_sorted[next_i] > pts_sorted[i]:
            gap = pts_sorted[next_i] - pts_sorted[i]
        else:
            gap = pts_sorted[next_i] + n - pts_sorted[i]
        if gap > max_gap:
            max_gap = gap
            start_index = next_i
    cyclic_order = [pts_sorted[(start_index + i) % len(pts_sorted)] for i in range(len(pts_sorted))]
    return cyclic_order

t_input = int(input())
for t in range(1, t_input + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    
    possible_ab = []
    possible_abcd = []
    
    for a in range(n):
        left_a, right_a = get_neighbors(a, n)
        for b in range(n):
            if b == a or b == left_a or b == right_a:
                continue
            possible_ab.append((a, b))
    
    for a, b in possible_ab:
        exclude = {a, b}
        exclude.update(get_neighbors(a, n))
        exclude.update(get_neighbors(b, n))
        
        possible_cd = [x for x in range(n) if x not in exclude]
        
        for c in possible_cd:
            left_c, right_c = get_neighbors(c, n)
            for d in possible_cd:
                if d == c or d == left_c or d == right_c:
                    continue
                possible_abcd.append((a, b, c, d))
    
    max_fitness = float('-inf')
    
    for quad in possible_abcd:
        pts = get_cyclic_order(list(quad), n)
        fitness = (arr[pts[0]] + arr[pts[3]])**2 + (arr[pts[1]] + arr[pts[2]])**2
        if fitness > max_fitness:
            max_fitness = fitness
            
    print(f"#{t} {max_fitness}")
