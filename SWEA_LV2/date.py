def day_of_year(month,day):
    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    return sum(months[:month-1])+day

Test_case=int(input())

for T in range(1,Test_case+1):

    month1,day1,month2,day2=map(int,input().split())

    days1=day_of_year(month1,day1)
    days2=day_of_year(month2,day2)

    print(f"#{T} {days2-days1+1}")