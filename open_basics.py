# Here we defined out open/close functions
def open_read_file(file):

    try:
        opened_file = open(file, 'r')
        print(type(file)) # not something we can work with
        file_lines_list = opened_file.readlines() # something we can worth
        print(file_lines_list)

        for line in file_lines_list:
            print(line.rstrip('\n'))

        opened_file.close() # This is what you do to your parents, otherwise file is locked and can't be changed

    except FileNotFoundError as errmsg:
        print('File cannot be found. Please check your inputs...', errmsg)
    except SyntaxError as errmsg:
        print('There has been a syntax error', errmsg)

open_read_file('order.txt')

def open_read_file_using_with(file):
    try:
        with open(file, 'r') as open_file:
            for line in open_file.readlines():
                print(line.rstrip('\n'))

    except FileNotFoundError as errmsg:
        print('File not found...', errmsg)

    finally:
        print('\n Execution Completed')

def write_to_file(file, order_item):
    try:
        with open(file, 'a') as opened_file:
            opened_file.write(order_item + '\n')

        opened_file.close()
    except FileNotFoundError:
        print('File not Found')

