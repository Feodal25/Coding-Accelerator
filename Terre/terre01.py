#file_path = __file__
#6
# print(file_path)
# print(len(file_path))
# print(file_path.index("/"))
# print(file_path[-1:"/"])
# print(file_path.find("/", 40, -1))



#------------------
# file_path = __file__
# file_name = ""
# number_of_slash = file_path.count("/")
# file_path_len = len(file_path)
# current_slash_index = 0
# current_slash = 0
# all_slash_index = []

# print(file_path)
# print(file_path_len)
# print(number_of_slash)
# print(file_path.index("/"))

# STOCKER INDEX DE TOUS LES "/" 
# file_path = __file__                            # /Users/gaetanlang/Desktop/Coding Accelerator/Coding-Accelerator/Terre/terre01.py
# slash_number = file_path.count("/")             # 7
# slash_index = []                                # 0, 6, etc
# last_slash_index = slash_index[slash_number]
#slash_index.append(file_path.index("/"))

# for slash_number in file_path:
#     current_slash_index = 0
#     slash_index.append(file_path.index("/", first_slash_index + current_slash_index))
#     current_slash_index = file_path.index("/")

#     print(file_path[last_slash_index:])


#print(file_path[last_slash_index + 1:])


# file_path = __file__
# list_slash_index = [0, 6, 17, 25, 44, 63, 69]
# last_slash_index = 69

# print(file_path.index("/", last_slash_index + 1))


#list_slash_index = [0]
# slash_number = file_path.count("/") 

# for i in file_path
# current_slash_index = 0
# list_slash_index.append(file_path.index("/", current_slash_index + 1))

# print(list_slash_index)

file_path = __file__
all_slash_index = [i for i, slash in enumerate(file_path) if slash == "/"]
slash_number = file_path.count("/")
last_slash_index = (all_slash_index[slash_number - 1])

print(file_path[last_slash_index + 1:])