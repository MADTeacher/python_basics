class CallTest:
    def __call__(self, *args, **kwargs):
        print("__call__")
        print(f"args = {args} \nkwargs = {kwargs}")

class CallTest2:
    def __call__(self, a, b, c=3):
        print("__call__")
        print(f"a = {a}, b = {b}, c = {c}")

if __name__ == "__main__":
    test = CallTest()
    test(10, 'Oo', 32.1)
    test(10, 'Oo', 32.1, a=2, b='-_-')

    test2 = CallTest2()
    test2(4, '^_^')
    test2(b=4, c=45.3, a='^_^')
    test2(8)