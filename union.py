		
def quickSort(alist,blist):
   quickSortHelper(alist,0,len(alist)-1,blist)

def quickSortHelper(alist,first,last,blist):
   if first<last:

       splitpoint = partition(alist,first,last,blist)

       quickSortHelper(alist,first,splitpoint-1,blist)
       quickSortHelper(alist,splitpoint+1,last,blist)


def partition(alist,first,last,blist):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
     	   temp2 = blist[leftmark]
           blist[leftmark] = blist[rightmark]
           blist[rightmark] = temp2

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   temp2 = blist[first]
   blist[first] = blist[rightmark]
   blist[rightmark] = temp2


   return rightmark

def max(a,b):
	if a>b:
		return a
	else:
		return b
   
def unionOfIntervals(alist,blist):
	for i in range(0,len(alist)-1):
		if alist[i+1] <= blist[i] :
			alist[i+1] = alist[i]
			blist[i+1] = max(blist[i],blist[i+1])
		else:
			print "("
			print alist[i] 
			print "," 
			print blist[i] 
			print ")"
	print alist[len(alist)-1]	
	print blist[len(alist)-1]



alist = [54,26,63,17,77,31,44,55,20]
blist = [58,34,100,47,78,34,45,78,37]
quickSort(alist,blist)
print(alist)
print blist
unionOfIntervals(alist,blist)
		
