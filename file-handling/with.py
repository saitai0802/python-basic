# with is just like using(aFileName as fileNameObject) in c#, It will call file.close() automatically afterwards.

# Not clean enough
file = open("/tmp/foo.txt")
data = file.read()
file.close()

# Clean code
if __name__ == '__main__':
    with open("/tmp/foo.txt") as file:
        data = file.read()


# Sai: Later on, you might check 'with' can also use for handle exception!
# Do a note later.
# http://blog.kissdata.com/2014/05/23/python-with.html
