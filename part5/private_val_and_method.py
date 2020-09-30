class PrivateTest:
    def __init__(self):
        self.public_x = "I'm public"
        self.__private_y = "I'm invisible"
        self._private_z = "I'm not invisible"

    def print_y(self):
        print(self.__private_y)

    def __get_y(self):
        return self.__private_y

if __name__ == "__main__":
    private_test = PrivateTest()
    print(private_test.public_x)
    print(private_test._private_z)
    private_test.print_y()
    #print(private_test.__private_y)
    print(private_test._PrivateTest__private_y)
    print(private_test._PrivateTest__get_y())
