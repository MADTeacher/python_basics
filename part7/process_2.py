from multiprocessing import Process

class MyProcess(Process):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self) -> None:
        print(f'Process #{self.args[0]} run with args = {self.args} '
              f'and kwargs = {self.kwargs}')


if __name__ == "__main__":
    for it in range(5):
        my_process = MyProcess(args=(it,),
                               kwargs={it: it+2, f"{it}": str(it)*2}
                               )
        my_process.start()
