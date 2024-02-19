# Initializing list
test_list = [1, 4, 5, 7, 8]
 
# Printing test_list
print("The list is : " + str(test_list))
 
# Finding length of list
# using sum()
list_len = sum(1 for i in test_list)
 
 
# Printing length of list
print("Length of list using len() is : " + str(list_len))
print("Length of list using length_hint() is : " + str(list_len))
