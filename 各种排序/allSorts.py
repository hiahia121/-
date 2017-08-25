#coding:utf-8
import time

def maopao(list1):
    '''
    冒泡排序
    相邻俩数，两两比较，逆序的话，互换位置，一轮下来，最大的数会被交换到最后
    :param list1:
    :return:
    '''
    for length in range(len(list1)-1,0,-1):
        for i in range(length):
            if list1[i] > list1[i+1]:
                temp = list1[i]
                list1[i] = list1[i+1]
                list1[i+1] = temp
    print list1

def quickSort(list1):
    '''
    快速排序
    基数x左侧都比它小，右侧都比它大。挖坑填数＋分治法
    :param list1:
    :return:
    '''
    less=[]
    pivotList=[]
    more=[]
    if len(list1)<=1:
        return list1
    else:
        pivot = list1[0]
        for i in list1:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)

        less = quickSort(less)
        more = quickSort(more)

        return less+pivotList+more

def insertSort(list1):
    '''
    直接插入排序
    将集合分为两部分，有序部分，和无序部分，将无序部分的第一个，不断的插入到有序的部分。首先选第一个有序的部分为集合第一个元素。
    :param list1:
    :return:
    '''
    for i in range(1,len(list1)):
        key = list1[i]
        j = i-1
        while j>=0:
            if list1[j]>key:
                list1[j+1]=list1[j]
                list1[j] = key
            j-=1
    print list1

def selectSort(list1):
    '''
    选择排序
    遍历数组，每次都将数组的第一个位置与后边的比较，筛选出最小的值，放在首位。
    :param list1:
    :return:
    '''
    for keyIndex in range(len(list1)-1):
        for i in range(keyIndex+1,len(list1)):
            if list1[i]<list1[keyIndex]:
                temp = list1[keyIndex]
                list1[keyIndex] = list1[i]
                list1[i] = temp
    print list1

def mergeSort(list1):
    '''
    归并排序
    分治法实现，归并思想是，两个集合a1,a2。结果集合a3，遍历比较a1，a2的第一个位置，将小的插入到a3。
    :param list1:
    :return:
    '''
    if len(list1)<=1:
        return list1
    mid = int(len(list1)/2)
    left = mergeSort(list1[:mid])
    right = mergeSort(list1[mid:])
    return merge(left,right)

def merge(left,right):
    '''
    归并排序
    合并两个集合，两个集合a1,a2。结果集合a3，遍历比较a1，a2的第一个位置，将小的插入到a3
    :param left:
    :param right:
    :return:
    '''
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result


def maxHeapify(ary,start,end):
    '''
    堆排序
    最大堆调整，将堆的末端子节点做调整，使得子节点永远小于父节点
    :param ary:
    :param start:为当前需要调整最大堆的位置
    :param end: 调整边界
    :return:
    '''
    root = start
    while True:
        child = root*2+1       #调整节点的子节点
        if child > end:
            break
        if child+1<=end and ary[child]<ary[child+1]:
            child = child+1      #取较大的子节点
        if ary[root]<ary[child]:       #较大的子节点成为父节点
            ary[root],ary[child] = ary[child],ary[root]      #交换
            root = child
        else:
            break

def heapSort(ary):
    '''
    堆排序
    :param ary:
    :return:
    '''
    n = len(ary)
    first = int(n/2-1)                  #最后一个非叶子节点
    for start in range(first,-1,-1):        #构造大根堆
        maxHeapify(ary,start,n-1)
    for end in range(n-1,0,-1):         #堆排序，将大根堆转换成有序数组
        ary[end],ary[0] = ary[0],ary[end]
        maxHeapify(ary,0,end-1)
    return ary

if __name__ == '__main__':
    list1 = [5,4,3,2,1]

    startTime1 = time.time()
    maopao(list1)
    print 'maopao use time '
    print time.time() - startTime1
    print '*'*100
    startTime2 = time.time()
    print quickSort(list1)
    print 'quickSort use time '
    print time.time() - startTime2
    print '*' * 100
    startTime3 = time.time()
    insertSort(list1)
    print 'insertSort use time'
    print time.time() - startTime3
    print '*' * 100
    startTime4 = time.time()
    selectSort(list1)
    print 'selectSort use time'
    print time.time() - startTime4
    print '*' * 100
    startTime5 = time.time()
    print mergeSort(list1)
    print 'merge use time'
    print time.time() - startTime5
    print '*' * 100
    startTime6 = time.time()
    print heapSort(list1)
    print 'heap use time'
    print time.time() - startTime6
    print '*'*100