class BaseTextTest:
    name = "Test"

    def set_text(self):
        self.text = "Class BaseTextTest"

    def print_base(self):
        return self.text

    def __str__(self):
        return self.text


class NewTextTest(BaseTextTest):
    def set_new_text(self):
        self.text = "Class NewTextTest"

    def print_new(self):
        return self.text

    def __str__(self):
        return self.text


if __name__ == "__main__":
    new_class = NewTextTest()
    def print_data():
        print(f'new_class = {new_class.name}, NewTextTest = {NewTextTest.name}, '
              f'BaseTextTest = {BaseTextTest.name}')
    new_class.set_text()
    print(new_class)
    print(new_class.print_base())
    print(new_class.print_new())
    new_class.set_new_text()
    print(new_class.print_new())
    print(new_class)

    print_data()
    NewTextTest.name = "Not bad"
    print_data()
    BaseTextTest.name = "Not good"
    print_data()
