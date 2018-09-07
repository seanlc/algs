# merge sort

# make one sorted list from two sorted lists
def sortTwoSortedLists(list1, list2):
    index1 = 0
    index2 = 0
    list3 = []
    lengthList1 = len(list1)
    lengthList2 = len(list2)
    while index1 < lengthList1 or index2 < lengthList2:
        if index1 == lengthList1:
            list3.append(list2[index2])
            index2 += 1
        elif index2 == lengthList2:
            list3.append(list1[index1])
            index1 +=1
        else:
            if list1[index1] < list2[index2]:
                list3.append(list1[index1])
                index1 += 1
            else:
                list3.append(list2[index2])
                index2 += 1
    return list3


# splits one list into two and returns as tuple
def partition(lst):
    p = len(lst)/2
    return(lst[:p], lst[p:])

# takes two unsorted lists as input and outputs a single sorted list
def mergeSort(l1, l2):
    s3 = []
    if len(l1) > 1:
        leftLsts = partition(l1)
        l1 = mergeSort(leftLsts[0], leftLsts[1])
    if len(l2) > 1:
        rightLsts = partition(l2)
        l2 = mergeSort(rightLsts[0], rightLsts[1])
    s3 = sortTwoSortedLists(l1,l2)
    return s3

list1 = [9,7,5,3,4]
list2 = [23,14,6,2,0]

print("list 1")
print(list1)
print("list 2")
print(list2)
list3 = mergeSort(list1, list2)
print("list3")
print(list3)
