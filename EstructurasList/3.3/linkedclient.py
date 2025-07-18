from linkedlistext import LinkedListExt
def main():
    linked_list = LinkedListExt()
    elem = [1,2,3,4,5,6,7,8,9,10]
    for i in elem:
        linked_list.append(i)
    ##Lista original
    print('Lista original:')
    print(linked_list)
    #iadd:
    linked_list.__iadd__([1,2,'Hola'])
    print('Lista luego de iadd:')
    print(linked_list)
    #addfirst:
    linked_list.add_first(2)
    print('Lista luego de addfirst:')
    print(linked_list)
    #pop
    linked_list.pop()
    print('Lista luego de pop:')
    print(linked_list)
    #Reverse:
    linked_list.__reversed__()
    print("Lista luego de reverse:")
    print(linked_list)

if __name__ == '__main__':
    main()