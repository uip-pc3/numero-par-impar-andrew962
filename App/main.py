def num(n1):
    if (n1%2==0):
        print('Numero Par')
        return 'Numero Par'
    else:
        print('Numero Impar')
        return 'Numero Impar'
"""
:param: todos:Prueba
:type: n1 int
:type: r int
:var: n1 es el cambio de nombre que sele la a la variable n del main
:var: r solo era para ver el resultado
"""


if __name__=="__main__":
    n = int(input('Introdusca numero: '))
    num(n)
    """
    :type: n int
    :var: n Se esta utilizando para guardar el numero introducidoy pasarlo a la funcion
    :param: num() funcion llamada para hacer el Calculo
    """