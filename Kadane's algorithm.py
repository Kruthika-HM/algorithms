#KADEN's algorithm to find maximum subarray
"""according to this algorithm it gives the contigious list of array elements which gives the maximum sum"""

def kd_algorithm(list_of_numbers):
    Max=0
    index=[]
    check=0
    if(list_of_numbers[0]<0):
        return max(list_of_numbers)
    #actual algorithm begins
    for inum,value in enumerate(list_of_numbers):
        if value>(value+check):
            check=value
        
            index.clear()
            index.append(inum)
        
        else:
            check=value+check
        if check>Max:
            index.append(inum)
            Max=check

    subarray=list_of_numbers[index[0]:index[-1]+1]
    return Max,subarray



#this portion deals with inputing a list of numbers
inputed_list=input("enter the comma seperated numbers only:")
modified_list=inputed_list.split(",")
try:
    list_of_numbers = [int(num_str) for num_str in modified_list]
except ValueError:
    print("invalid input")

result=kd_algorithm(list_of_numbers)
print(f"the maximum sum and subarray of the given list is: {result}")






