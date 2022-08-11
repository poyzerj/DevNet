my_number_of_path = [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 4, 2]

my_multipath_list = []

for paths in my_number_of_path:
    if paths > 5:
        my_multipath_list.append(paths)

if my_multipath_list:
    print(my_multipath_list)
else:
    print("There were no multipath values")