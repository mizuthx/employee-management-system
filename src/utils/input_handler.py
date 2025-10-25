from datetime import date
from time import sleep

def x_input(tipo: str, p:str = 'Opcion'):
    """
    Valida el tipo de dato que se indique.
    str:   lorem Ipsum
    int:   123
    float: 3.14
    date:  DD / MM / YYYYY
    ?:     S/N
    """
    def y_or_not():
        while True:
            x = str(input('(S/N): ')).lower()
            if x == 's':
                return True
            elif x == 'n':
                return False
            else:
                print("Entrada Invalida...")
    def x_date():
        def ddmmyyy():
            pass
        
        fecha:list = []
        for i in range(1,4):
            if i == 1:
                fecha.append(int(input('DIA: ')))
            elif i == 2:
                fecha.append(int(input('MES: ')))
            elif i == 3:
                fecha.append(int(input('AÑO: ')))
        tmp = date(fecha[2], fecha[1], fecha[0])
        return tmp
    tipos:dict = {
        'str': str,
        'int': int,
        'float': float,
        'date': date,
        '?': "question"
    }
    if tipo in tipos:
        try:
            if tipos[tipo] == str:
                tmp = str(input(p + ': '))
                return tmp
            elif tipos[tipo] == int:
                tmp = int(input(p + ': '))
                return tmp
            elif tipos[tipo] == float:
                tmp = float(input(p + ': '))
                return tmp
            elif tipos[tipo] == 'question':
                tmp = y_or_not()
                return tmp
            elif tipos[tipo] == date:
                tmp = x_date()
                return tmp
        except ValueError as e:
            print("Entrada Invalida\n" + e)
    else:
        print('Tipo de dato no valido')
    
if __name__ == '__main__':
    tmp = x_input('date')
    print(tmp)