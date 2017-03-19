def minutes(A,B):
    sum = A + (B * 10)
    total= -1
    if sum<60:
        total = sum
    sum = B + (A * 10)
    if sum<60 and total<sum:
        total = sum
    return total

def hours(A,B):
    sum = A + (B * 10)
    total= -1
    if sum<24:
        total = sum
    sum = B + (A * 10)
    if sum<24 and total<sum:
        total = sum
    return total

def Solution(A,B,C,D):
    num = [A,B,C,D]
    num.sort(reverse=True)
    length = len(num)
    time = "invalid"
    a = 0
    myList = []
    while a < length-1:
        if hours(num[a],num[a+1]) > -1:
            myList.append(num[a])
            myList.append(num[a+1])
            a = length
        else:
            a = a + 1
    if len(myList)>0:
        num.remove(myList[0])
        num.remove(myList[1])
        if minutes(num[0], num[1]) > -1 and hours(myList[0],myList[1])> -1:
            xyz= hours(myList[0],myList[1])
            abc = minutes(num[0], num[1])
            time = str(xyz) + ":" + str(abc)
    return time

print Solution(2,3,5,8)