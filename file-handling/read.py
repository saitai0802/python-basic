# You can use open method in python shell
# That file will be locked if console is still opening.
# Need to close that file to save changes(in writing mode) and release file.
file = open("./example_r.txt", "r")
content = file.read()
print(content) # print all content inside txt file.

print("==========Start of Understand pointer=========")
content = file.readline()
print(content) # print nothing

# Because the pointer of file object has reached the last position when file.read()
# When file.readline() process. It start to read a line from the last position.
# That is why print our file.readline() content has nothing to return.
# Solution: We needa to reset the point.
print("==========End of Understand pointer=========")

file.seek(0) # Set pointer to Zero
content = file.readlines()
print(content)
# print ['Line 1\n', 'Line 2\n', 'Line 3\n', 'Line 4\n', 'Line 5\n', 'Line 6']

#
content = [i.rstrip("\n") for i in content]
print(content)
# ['Line 1', 'Line 2', 'Line 3', 'Line 4', 'Line 5', 'Line 6']

input('Press ENTER to exit') # <== This python-syntax proof file if keep open in script level!
file.close()
# Opening a file in console need to use file.close()