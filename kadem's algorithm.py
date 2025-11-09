#KADEN's algorithm to find maximum subarray
"""according to this algorithm it gives the contigious list of array elements which gives the maximum sum"""

#this portion deals with inputing a list of numbers
inputed_list=input("enter the comma seperated numbers only:")
modified_list=inputed_list.split(",")
try:
    list_of_numbers = [int(num_str) for num_str in modified_list]
except ValueError:
    print("invalid input")
    
#actual algorithm begins
max=0
index=[]
check=0
for inum,value in enumerate(list_of_numbers):
    if value>(value+check):
        check=value
        
        index.clear()
        index.append(inum)
        
    else:
        check=value+check
    if check>max:
        
        index.append(inum)
        max=check

subarray=list_of_numbers[index[0]:index[-1]+1]
print(index)
print(f"the maximum sum is:{max}")
print(f"the maximum subarray is:{subarray}")





