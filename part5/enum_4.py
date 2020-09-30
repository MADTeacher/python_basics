from enum import IntFlag

class TestFlag(IntFlag):
    A = 1
    B = 2
    C = 3
    D = 4

if __name__ == "__main__":
    print(repr(TestFlag.A | TestFlag.B))
    RW = TestFlag.A | TestFlag.D
    print(repr(RW))
    print(TestFlag.A in RW)
    print(repr(TestFlag.D & TestFlag.C))
    print(repr(TestFlag.D ^ TestFlag.C))


    print(bool(TestFlag.D & TestFlag.C))

    print(repr(TestFlag.D ^ 12))
    print(repr(TestFlag.A | 6))