class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, *args):
        if len(args) == 3:
            start = args[0]
            stop = args[1]
            step = args[2]
        elif len(args) == 2:
            start = args[0]
            stop = args[1]
            if start > stop:
                step = -1
            else:
               step = 1
        elif len(args) == 1:
            step = 0
            raise StepValueError('Не указан шаг итерации и конечное значение')
        else:
            raise StepValueError('Слишком много аргументов')


        if step == 0:
            raise StepValueError('Шаг указан неверно')
        elif step is None:
            if start > stop:
                step = -1
            else:
                step = 1


        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        result = self.pointer
        self.pointer += self.step
        return result


if __name__ == '__main__':

    args_list = [[100, 200, 0], [-5, 1], [6, 15, 2], [5, 1, -1], [10 ,1], [10, 20, 1, 6, 7], [10]]
    iter_list = []
    for i in args_list:
        try:
            if len(i) > 1:
                iter_list.append(Iterator(*i))
            else:
                iter_list.append(Iterator(i[0]))
        except StepValueError as exc:
            print(f' {exc.args[0]}' )

    for i in iter_list:
        for j in i:
            print(j, end=' ')
        print()

