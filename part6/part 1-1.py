class TestException(Exception):
    logfile = 'dataerror.txt'

    def __init__ (self, line, file) :
        self.line = line
        self.file = file

    def logerror(self):
        log = open(self.logfile, 'a')
        print('Error at:', self.file, self.line, file=log)

def test():
    try:
        raise TestException(22, 'test.log')
    except TestException as my_ex:
        my_ex.logerror()
        print(my_ex)

if __name__ == "__main__":
    test()