#Interpolation Search

'''
Note : 
	- Data must be sorted.
	- Data must be sequential Ex. 1 3 5 7 // Differance between each element 2.
	
How it works ?
- Assume that you have one book with 500 pages. 
  
  CASE 1 :
	someone tells you to open page no.400 
	So In this case You definitely turn your books pages from the end.
	
 
  CASE 2 :
	someone tells you to open page no.20 
	So In this case You definitely turn your books pages from the start.
	
	
Why this algo ?
- It works more efficient than Binary Search.


Note :
If your data is not sorted and not sequential Still my Code work Perfectly.

#THANK YOU
'''

def sort_data(data):
	data.sort()
	pass
	
	
def interpolation_search(data,search):
	if search in data:
		low = 0
		high = len(data) - 1
		pos = int (low + (( search - data[low]) / (data[high] - data[low])) * (high - low))
		print(f"Postion : { pos }")
	
		while(data[pos] != search):
			if data[pos] > search :
				pos = pos - 1
			else:
				pos = pos + 1
		else:
			return pos
			#print("Final : " ,pos)
	else:
		return -1
	
	
if __name__ == "__main__":
	data = []
	size = int(input("How many elements you want to enter : "))
	print(f"\n--------------------Initializing-------------------")
	for i in range(size):
		temp = int(input(f"Enter element { i+1 } : "))
		data.append(temp)
		
	search = int(input(f"\nEnter element for search : "))
	sort_data(data)
	print(f"Data is : { data }")
	print(f"Search for : { search }")
	index = interpolation_search(data,search)
	
	if index != -1:
		print(f"\nINDEX OF SEARCHED ELEMENT :{ index}")
		print(f"\nSEARCHED ELEMENT IS : { data[index] }")
	else:
		print(f"\nSearched Element is not present in Data.")