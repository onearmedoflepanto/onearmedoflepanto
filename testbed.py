# t_input = int(input())

# for t in range(1, t_input+1):
#     n = int(input())
#     a = []
#     b = []
#     for _ in range(n):
#         a_val, b_val = map(int, input().split())
#         a.append(a_val)
#         b.append(b_val)

#     p = int(input())

#     c = []

#     for _ in range(p):
#         c_val = int(input())
#         c.append(c_val)

#     dat = [0] * 5001

#     for i in range(n):
#         for j in range(a[i], b[i]+1):
#             dat[j] += 1

#     print(f"#{t}", end=' ')
#     for num in c:
#         print(dat[num], end=' ')

# new test code for github push

# import heapq

# n= int(input())

# pq_max = []
# pq_min = []

# heapq.heappush(pq_min, 500)

# for _ in range(n):
#     a, b = map(int, input().split())

#     for num in [a, b]:
#         if not pq_max or num <= -pq_max[0]:
#             heapq.heappush(pq_max, -num)
#         else:
#             heapq.heappush(pq_min, num)

#     if len(pq_max) > len(pq_min) + 1:
#         heapq.heappush(pq_min, -heapq.heappop(pq_max))
#     elif len(pq_min) > len(pq_max):
#         heapq.heappush(pq_max, -heapq.heappop(pq_min))

#     print(-pq_max[0])

# import heapq

# q_num = int(input())
# q_list = list(map(int, input().split()))
# q_list.sort()
# n = max(q_list)


# def get_ugly_numbers(n):
#     heap = [1]
#     seen = {1}  # 중복 방지를 위한 집합
#     ugly_numbers = []

#     for _ in range(n):
#         # 힙에서 가장 작은 값을 꺼냅니다.
#         ugly = heapq.heappop(heap)
#         ugly_numbers.append(ugly)

#         # 2, 3, 5를 곱한 값을 힙에 추가합니다.
#         for factor in [2, 3, 5]:
#             new_val = ugly * factor
#             if new_val not in seen:
#                 seen.add(new_val)
#                 heapq.heappush(heap, new_val)

#     return ugly_numbers


# ugly_numbers = get_ugly_numbers(n)

# for q in q_list:
#     print(ugly_numbers[q - 1], end=' ')

# n = int(input())
# str_num = input()

# print(sum(int(char) for char in str_num))


# n = int(input())

# for _ in range(n):
#     cents = int(input())

#     coin_lst = [25, 10, 5, 1]
#     coin_num_lst = []

#     for coin in coin_lst:
#         coin_num_lst.append(cents // coin)
#         cents %= coin

#     print(*coin_num_lst)

# x = int(input())
# total = 0
# i = 1

# while total < x:
#     total += i
#     i += 1

# i -= 1  # 마지막 i가 한 번 더 증가했으므로 감소시킴
# x -= (total - i)  # x를 정확한 위치로 보정

# # (1,1)부터 시작하도록 조정
# i_arr = [(i - j + 1, j) for j in range(1, i + 1)]

# if i % 2 == 1:
#     num, den = i_arr[x - 1]
#     print(f"{num}/{den}")
# else:
#     num, den = i_arr[i - x]
#     print(f"{num}/{den}")

# n = int(input())

# arr = [input() for _ in range(n)]

# res = []

# for j in range(len(arr[0])):
#     compare = arr[0][j]
#     flag = True
#     for i in range(1, len(arr)):
#         if arr[i][j] != compare:
#             flag = False
#             break

#     if flag:
#         res.append(compare)
#     else:
#         res.append("?")

# print(''.join(res))

arr = list(map(int, input().split()))
arr.sort(reverse=True)

if arr[0] <= arr[1] + arr[2]:
    print(sum(arr))

else:
    arr[0] = (arr[1] + arr[2]) * 2 - 1
    print(sum(arr))
