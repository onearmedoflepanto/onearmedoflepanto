t_input=int(input())

for t in range(1,t_input+1):
    n=int(input())
    arr=input()
    arr_num=[int(chr) for chr in arr]
    
    counter=0
    count_max=0
    max_number=0

    for num in arr_num:
        for sch_num in arr_num:
            if num == sch_num:
                counter +=1

        if counter >= count_max:
            count_max = counter
            if num > max_number:
                max_number = num
        
        counter = 0

    print(f"#{t} {max_number} {count_max}")