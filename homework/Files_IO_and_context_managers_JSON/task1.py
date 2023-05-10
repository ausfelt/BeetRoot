with open("myfile.txt", "w") as f:
    f.write("Hello file world!\n")

with open("myfile.txt", "r") as f:
    contents = f.read()
    print(contents)


# python create_file.py
# python read_file.py
# Use these two if you want to run it from the terminal