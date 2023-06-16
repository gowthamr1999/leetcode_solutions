def find_index(cards,number):
    start = 0
    end = len(cards)-1
    while(start<=end):
        mid = (end+start)//2
        mid_number = cards[mid]
        if number == mid_number:
            return mid
        elif number > mid_number:
            end = mid-1
        elif number< mid_number:
            start = mid+1
    return -1




def liner_search(cards,number):
    for i in range(len(cards)):
        if cards[i] == number:
            return i
    else:
        return "Not found"


from datetime import datetime
start_time = datetime.now()
print(find_index(cards = [9,8,6,3,2,1,0],number = 6))
print(datetime.now() - start_time)

start_time = datetime.now()
print(liner_search(cards = [9,8,6,3,2,1,0],number = 6))
print(datetime.now() - start_time)