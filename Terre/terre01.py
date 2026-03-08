file_path = __file__
all_slash_index = [i for i, slash in enumerate(file_path) if slash == "/"]
slash_number = file_path.count("/")
last_slash_index = (all_slash_index[slash_number - 1])

print(file_path[last_slash_index + 1:])