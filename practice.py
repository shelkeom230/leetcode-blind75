def quickSort(arr,low,high):
	if low<high:
		pindex=partition(arr,low,high)

		quickSort(arr,low,pindex)
		quickSort(arr,pindex+1,high)
		return arr

def partition(arr,low,high):
	pivot=arr[low]
	i=low
	j=high

	while i<j:
		while arr[i]<=pivot and i<=high-1:
			i+=1
		while arr[j]>pivot and j>=low+1:
			j-=1

		if i<j:
			arr[i],arr[j]=arr[j],arr[i]

	arr[low],arr[j]=arr[j],arr[low]
	return j

arr=[3,2,1]
low=0
high=len(arr)-1
print(quickSort(arr,low,high))