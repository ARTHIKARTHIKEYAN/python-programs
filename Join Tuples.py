def join_similar_initial_elements(tuple_list):
    result_dict = {}
    
    for tpl in tuple_list:
        initial_element = tpl[0]
        
        if initial_element in result_dict:
            result_dict[initial_element] += tpl[1:]
        else:
            result_dict[initial_element] = tpl
    
    result_list = list(result_dict.values())
    
    return result_list

# Example usage
tuple_list = [(1, 'apple'), (2, 'banana'), (1, 'orange'), (3, 'grape'), (2, 'kiwi')]

joined_tuples = join_similar_initial_elements(tuple_list)

print("Original Tuple List:", tuple_list)
print("Joined Tuples:", joined_tuples)
