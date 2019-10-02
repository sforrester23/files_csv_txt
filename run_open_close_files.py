from open_basics import *

# here we'll run all our functions
open_read_file('order.txt')
print('////')
open_read_file_using_with('order.txt')
print('////')
item_list = ['paella', 'burgers', 'pizza']
for item in item_list:
    write_to_file('order.txt', item)

