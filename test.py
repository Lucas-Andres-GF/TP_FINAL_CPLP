# Creamos nuestra propia excepción heredando
# de la clase Exception
class MiExcepcionPersonalizada(Exception):
    def __init__(self, parametro1, parametro2):
        self.parametro1 = parametro1
        self.parametro2 = parametro2
# Lanzamos con raise la excepción que hemos creado
try:
    raise MiExcepcionPersonalizada("Hola", "Chau")
except MiExcepcionPersonalizada as ex:
    p1, p2 = ex.args
    # print(type(ex))
    # print("parametro1 =", p1)
    print('parametros {}'.format(list(map (lambda x: x, ex.args))))

#<class '__main__.MiExcepcionPersonalizada'>
#parametro1 = ValorPar1
#parametro2 = ValorPar2