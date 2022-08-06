# Printing range of numbers without using loops 
def print_numbers(start , end ):
    print(start)
    return  print_numbers(start+1, end)  if end > start else print("End")
        
print_numbers(1, 12)