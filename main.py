class Stack:
    def __init__(self, certain_input: str):
        self.certain_list = list(certain_input)

    def is_empty(self):
        if self.certain_list:
            return True
        else:
            return False

    def push(self, element: str):
        self.certain_list.append(element)

    def pop(self):
        self.certain_list.pop(-1)
        return self.certain_list[-1]

    def size(self):
        size = len(self.certain_list)
        return size

    def for_test(self, middle):
        first_half = self.certain_list[:middle]
        reverse_list = []
        for i in first_half:
            if i == '(':
                i = ')'
            elif i == '[':
                i = ']'
            else:
                i = '}'
            reverse_list.append(i)
        second_half = self.certain_list[middle:]
        return reverse_list, second_half


if __name__ == "__main__":
    certain_list = input('Введите строку скобок: ')
    element = input('Введите дополнительный элемент: ')
    certain_list = Stack(certain_list)
    print(Stack.is_empty(certain_list))
    print(Stack.push(certain_list, element))
    print(Stack.pop(certain_list))
    print(Stack.size(certain_list))

    middle = round(Stack.size(certain_list) / 2)
    reverse_list, second_half = Stack.for_test(certain_list, middle)
    if reverse_list == second_half:
        print('Сбалансированно')
    else:
        print('Несбалансированно')
