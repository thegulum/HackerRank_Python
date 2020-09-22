list1 = []
operator_numbers = int(input("add number of operators : "))
for number in range(operator_numbers):
    command = input()
    list2 = command.split(" ")
    if list2[0] == 'append':
        list1.append(list2[1])
    elif list2[0] == 'print':
        print(list1)
    elif list2[0] == 'remove':
        list1.remove(list2[1])
    elif list2[0] == 'insert':
        list1.append(list2[1])
    elif list2[0] == 'sort':
        list1.sort()
    elif list2[0] == 'pop':
        list1.pop()
    elif list2[0] == 'reverse':
        list1.reverse()
