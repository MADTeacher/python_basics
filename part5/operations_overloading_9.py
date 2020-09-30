class MyTruth:
    def __bool__(self):
        return True

class MyTruth2:
    def __len__(self):
        return 0

class MyTruth3:
    def __bool__(self):
        return True

    def __len__(self):
        return 0

class TestTruth: ...

if __name__ == "__main__":
    my_truth = MyTruth()
    if my_truth: print("True")
    my_truth2 = MyTruth2()
    if not my_truth2: print("True")
    my_truth3 = MyTruth3()
    if my_truth3: print("True")
    test = TestTruth()
    print(bool(test))