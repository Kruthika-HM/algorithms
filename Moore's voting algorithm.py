# This algorithm finds the majority element in an array with time complexity of O(n) and space complexity of O(1)
""" majority element is the one which is repeated more than length of array//2 times in an array"""

def moore_voting(array):
    freq=0
    check=None
    num=len(array)//2
    for i in array:
        if freq==0:
            check=i
            freq=1
        elif check==i:
            freq+=1
        else:
            freq-=1 
    if array.count(check)<=num:
        print("No majority element")
    return check

array=[1,2,2,1,2,3,2,2]
result=moore_voting(array)
print(f"The majority element is: {result}")
    

    
