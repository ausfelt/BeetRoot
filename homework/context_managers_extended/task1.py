import logging


class MyOpen:

    counter = 0

    def __init__(self, file_name, mode="r+"):
        self.file_object = open(file_name, mode)
        self.mode = mode

    def __enter__(self):
        MyOpen.counter += 1
        return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            logging.exception("Exception handled")
        self.file_object.close()