# this function will take two arguments 

# If the target is in the list then we return it's position.
# The linear search is a sequential search 
def linear_search(list,target):
    '''Take Two Arguments (List) and (target)'''
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print('Target found at index NO: ',index)
    else:
        print("Target Not found.")


numbers=[1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers,2)
verify(result)



