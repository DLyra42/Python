def findEven(n):
    r = (n%2==0)
    return r

def sumEven(lst):
    sum=0
    for num in lst:
        if(findEven(num)):
            sum=sum+num
    return sum

list = [10, 2, 5, 7, 6, 3]
sum = sumEven(list)
print(f'The sum of the even elements of the list is: {sum}')