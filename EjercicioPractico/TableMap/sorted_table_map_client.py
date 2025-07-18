from SortedTableMap import SortedTableMap
from data_structures import MapBase
table = SortedTableMap()
def main():
    
    table['Argentina'] = 'Pesos'
    table['Brasil']    = 'Reales'
    table['España']    = 'Euros'
    table['China']     = 'Yuan'
    table['Peru']      = 'Euros'
    print('Mapeo original:')
    print(table)
    #SetItem:
    table.__setitem__('Peru','Soles')
    print('Mapeo luego del item setiado')
    print(table)
    #GetItem:
    item = table.__getitem__('Peru')
    print(f'Item solicitado: {item}')
    #DeleteItem:
    table.__delitem__('China')
    print('Mapeo luego de la eliminacion')
    print(table)
    #Iters:
    items=table.iter_items()
    keys =table.__iter__()
    print('Items:')
    for i in items:
        print(i)
    print('Claves:')
    for i in keys:
        print(i)
    
   
    
if __name__ == '__main__':
    main()