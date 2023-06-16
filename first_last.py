def binary_search(list1,target,first,last,condition):
    while(first<=last):
        mid = (first+last)//2
        result =  condition(mid)
        if result == "Found":
            print(mid)
            break
        
        elif result == "left":
            last = mid-1

        else:
            first = mid +1

def first_position():
    list1 = [5,6,8,8,10]
    target = 8
    first = 0
    last = len(list1)-1
    def firstcondition(mid):
        if list1[mid] == target:
            if list1[mid-1] == target and mid>0:
                return "left"
            else:
                return "Found"
        
        
        elif list1[mid] < target:
            return "right"
        
        elif list1[mid] > target:
            return "left"
        
    binary_search(list1,target,first,last,firstcondition)
    


def last_position():
    list1 = [5,6,8,8,10]
    target = 8
    first = 0
    last = len(list1)-1
    def lastcondition(mid):
        if list1[mid] == target :
            if list1[mid+1] == target and mid<len(list1):
                return "right"
            else:
                return "Found"
        
        elif list1[mid] < target:
            return "right"
        
        elif list1[mid] > target:
            return "left"
    binary_search(list1,target,first,last,lastcondition)
    

first_position()
last_position()