# ****Keep in mind****
# We don't need to file.close because our python console life cycle will be ended at the last line of our code!

# If file is not existed, create it.
# w mode means write. (Overwriting the whole file)
# a mode means append. (Append new lines form the tail of a  file)
file = open("example_w.txt", "w")
file.write("Line 1")
file.write("Line 2")
# file: Line 1Line 2

file.seek(0)
lines = ['Line1', "Line 2", "Line 3"]
for single_line in lines:
    file.write(single_line + "\n")
# file:
# Line 1
# Line 2
# Line 3