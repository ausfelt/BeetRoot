from task1 import MyOpen

with MyOpen("text_test.txt", "a+") as file_obj:
    file_obj.write("Look! Even more text!\n")

with MyOpen("text_test.txt", "r+") as file_obj:
    load = file_obj.read()
    print(load)