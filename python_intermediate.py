#################
# Lists
#################
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list[::2]) # every item with step=2
print(my_list[::-1]) # in reverse order

new_list = my_list # if you change new_list, my_list will also change
new_list = my_list.copy() # if you change new_list, my_list will stay the same
new_list = list(my_list) # if you change new_list, my_list will stay the same
new_list = my_list[:] # if you change new_list, my_list will stay the same

#################
# Tuples
#################

# ways to create
my_tuple = (1, 2, 3, 4)
my_tuple = 1, 2, 3, 4
my_tuple = (1,)
my_typle = typle(my_list)

my_tuple[0] = 'Other' # can't do this

i1, *i2, i3 = my_tuple
print(i1) # 1
print(i2) # [2, 3]
print(i3) # 4

# comparing speed of creating list vs tuple
import timeit
print(timeit.timeit(stmt='[0, 1, 2, 3, 4]', number=1000000))
print(timeit.timeit(stmt='(0, 1, 2, 3, 4)', number=1000000))

#################
# Dictionaries
#################
