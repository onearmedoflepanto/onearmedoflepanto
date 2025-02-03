T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    strings = [input().strip() for _ in range(N)]
    
    freq = {}
    for s in strings:
        freq[s] = freq.get(s, 0) + 1

    total_length = 0  
    center_length = 0 
    used = set()
    
    for s in list(freq.keys()):
        if s in used:
            continue
        
        rev = s[::-1]
        if s == rev:
            total_length += (freq[s] // 2) * 2 * len(s)
            if freq[s] % 2 == 1:
                center_length = max(center_length, len(s))
            used.add(s)
        else:
            if rev in freq:
                pair_count = min(freq[s], freq[rev])
                total_length += pair_count * 2 * len(s)
                used.add(s)
                used.add(rev)
    
    result = total_length + center_length
    print(f"#{t} {result}")