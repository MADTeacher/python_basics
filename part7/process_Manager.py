from multiprocessing import Process, Manager, Event


def slave(ns, event):
    ns.my_list.append(1)
    ns.my_list.append(2)
    ns.my_list.append(3)
    ns.my_list.append("new value")
    ns.my_value = 3.14
    event.set()


def master(ns, event):
    print(f'my_list до установки флага события: {ns.my_list}')
    print(f'my_value до установки флага события: {ns.my_value}')
    event.wait()
    print(f'my_list после установки флага события: {ns.my_list}')
    print(f'my_value после установки флага события: {ns.my_value}')


if __name__ == '__main__':
    mgr = Manager()
    namespace = mgr.Namespace()  # общее пространство имен
    namespace.my_list = mgr.list()
    namespace.my_value = mgr.Value('d', 0.0)

    event = Event()
    slave_process = Process(
        target=slave,
        args=(namespace, event),
    )
    master_process = Process(
        target=master,
        args=(namespace, event),
    )

    master_process.start()
    slave_process.start()

    master_process.join()
    slave_process.join()