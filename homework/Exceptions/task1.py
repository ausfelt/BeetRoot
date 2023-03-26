class Klass:
    some_attr = "Klass"
    # Klass has its namespace. It's stored in Klass.__dict__.
    # And after we said some_attr = "Klass" Klass.__dict__ got a record {"some_attr": "Klass"}

    def __init__(self):
        self.some_attr = "not Klass"
        # we create an instance, and its __dict__ is going to receive {"some_attr": "not Klass"}

    def print_some_attr(self):
        print(self.some_attr)

    @classmethod
    def print_some_class_attr(cls):
        print(cls.some_attr)


klass_instance = Klass()
klass_instance.print_some_attr()
klass_instance.print_some_class_attr()
klass_instance.

