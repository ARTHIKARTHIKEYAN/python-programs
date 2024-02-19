import heapq
test_tup = (5, 20, 3, 7, 6, 8)
# printing original tuple
print("The original tuple is : " + str(test_tup))
K = 2
smallest = heapq.nsmallest(K, test_tup)
largest = heapq.nlargest(K, test_tup)
result = tuple(sorted(smallest + largest))
print("The extracted values : " +str(result))
