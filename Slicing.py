# Slicing
#  It allows you to efficiently access specific parts of the data without modifying the original sequence.

my_list = [0,1,2,"Asad","Syed Haziq",5.4,True]

print(my_list[1:4])

print(my_list[::2])  # Output: [0, 2, 'Syed Haziq', True] (every second element)

print(my_list[::-1])
