


def binarySearch(array,key,start,end):
    if(start>end) : return -1

    mid = (start+end)//2

    if key==array[mid]:
        return mid
    elif key<array[mid]:
        return binarySearch(array,key,start,mid-1);
    else:
        return binarySearch(array,key,mid+1,end)

if __name__=='__main__':
    array = [1,3,7,11,12,14,18]
    start = 0
    end = len(array)-1
    key = 0
    print(binarySearch(array,key,start,end))