from LinkedStackExt import LinkedStackExt
from data_structures import LinkedStack
Stack = LinkedStack()
def main():
        #CARGAR LA PILA CON DATOS:
        elem = [1,2,3,4,5,6,7,8,9,10]
        StackExt = LinkedStackExt()
        for i in elem:
            StackExt.push(i)
            Stack.push(i)
        print('Stack original:')
        print(StackExt)
        #Imul:Repite tantas veces como lo indique other los elmentos actuales de la pila y los inserta al final de la misma
        StackExt.__imul__(1)
        print('Stack luego del metodo imul:')
        print(StackExt)
        #Replace all:Reemplaza todas las ocurrencias de param1 en la pila por param2
        StackExt.replace_all(1,2)
        print('Stack luego del metodo replace_All: ')
        print(StackExt)
if __name__ == '__main__':
    main()

    

    