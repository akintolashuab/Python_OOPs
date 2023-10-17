# with open ("Example.txt", "a") as file:
#         file.write("\nAppending additional content")
#         file.write("\nAppending more additional content")


with open("Data.csv", "r") as my_files:
        words_length = [len(i.split(',')) for i in my_files.readlines()]
        print(words_length)
new_list = ["item"+str(i) for i in range(1, max(words_length)+1)]
print(new_list)