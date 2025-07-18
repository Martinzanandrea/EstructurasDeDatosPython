from data_structures import BinaryTreeNode
from LinkedBinaryTreeExt import LinkedBinaryTreeExt

def main() :
    nodo_a = BinaryTreeNode('A')
    nodo_b = BinaryTreeNode('B')
    nodo_c = BinaryTreeNode('C')
    nodo_d = BinaryTreeNode('D')
    nodo_f = BinaryTreeNode('F')
    nodo_g = BinaryTreeNode('G')
    nodo_h = BinaryTreeNode('H')
    nodo_i = BinaryTreeNode('I')
    nodo_k = BinaryTreeNode('K')
    nodo_m = BinaryTreeNode('M')
    nodo_n = BinaryTreeNode('N')
    arbol = LinkedBinaryTreeExt()
    arbol.add_root(nodo_a)
    arbol.add_left_child(nodo_a, nodo_b)
    arbol.add_right_child(nodo_a, nodo_f)
    arbol.add_left_child(nodo_b, nodo_c)
    arbol.add_right_child(nodo_b, nodo_d)
    arbol.add_left_child(nodo_f, nodo_g)
    arbol.add_right_child(nodo_f, nodo_k)
    arbol.add_left_child(nodo_g, nodo_h)
    arbol.add_right_child(nodo_g, nodo_i)
    arbol.add_left_child(nodo_k, nodo_m)
    arbol.add_right_child(nodo_k, nodo_n)
    #Ancestro mas inmediato entre 2 nodos:
    ancestro = arbol.ancestro_mas_inmediato(nodo_c,nodo_n)
    print(f'Ancestro mas inmediato de {nodo_c} y {nodo_n} es  {ancestro}') 
    #Hojas del arbol:
    hojas = arbol.hojas()
    print(f'Hojas del arbol:  {hojas}')
    #Diametro del arbol
    diametro = arbol.diametro()
    print(f'Diametro del arbol: {diametro}')
    #Nivel del nodo buscado:
    nivel = arbol.nivel(nodo_m)
    print(f'Nivel del nodo buscado: {nivel}')
    #Verificar si el arbol esta balanceado:
    balanceado = arbol.es_balanceado()
    print(f'Arbol balanceado(True:si/False:no): {balanceado}')
    
if __name__ == '__main__':
    main()
    
