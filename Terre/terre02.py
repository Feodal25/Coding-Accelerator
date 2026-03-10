import sys
args_without_filename = sys.argv[1:]   

# index = 0
# while index < len(args_without_filename):
#     print(args_without_filename[index])
#     index += 1

for arg in args_without_filename:
    print(arg)