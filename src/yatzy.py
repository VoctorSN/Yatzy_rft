
"""
    Modulo de la clase yatzy
    En este modulo hay 1 clase
    yatzy y detro de ella hay diferentes
    funciones/metodos, cada uno
    de ellos es un metodo de puntuaje
    del juego yatzy,
    todos estos metodos tienen
    como argumento una lista de enteros que
    son los dados del juego,
    dependiendo de los dados que salgan 
    y el metodo de puntuaje que elijas
    obtendras mas o menos puntos 
"""
if __name__ == "__main__":

    from pips import Pips

else:

    from src.pips import Pips

class Yatzy:

    """
    clase yatzy con los metodos
    de puntuaje
    """
    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        """
        devuelve un entero,
        la suma de todos los dados
        """
        return sum(dice)

    @staticmethod
    def yatzy(*dice):
        """
        la funcion set crea
        un tipo de objeto que es
        como una lista pero sin repetidos,
        por tanto si el dice sin repetidos
        tiene 1 de latgo esto significa que
        todo el dice esta formado por 1 unico
        numnero repetido
        """
        return 50 if len(set(dice)) == 1 else 0

    @staticmethod
    def ones(*dice):
        """
        suma 1 punto por cada 1 que salga
        """
        return dice.count(1)

    @staticmethod
    def twos(*dice):
        """
        suma 2 puntos por cada 2 que salga
        """
        return dice.count(2) * 2

    @staticmethod
    def threes(*dice):
        """
        suma 3 puntos por cada 3 que salga
        """
        return dice.count(3) * 3

    @staticmethod
    def fours(*dice):
        """
        suma 4 puntos por cada 4 que salga
        """
        return dice.count(4) * 4

    @staticmethod
    def fives(*dice):
        """
        suma 5 puntos por cada 5 que salga
        """
        return dice.count(5) * 5

    @staticmethod
    def sixes(*dice):
        """
        suma 6 puntos por cada 6 que salga
        """
        return dice.count(6) * 6

    @classmethod
    def pair(cls,*dice):
        """
        crea una lista sin repetidos
        con todos los numeros que aparecen
        2 o mas veces y los multiplica por 2,
        si no hay repetidos puntua 0
        """
        return (cls.biggest_pip_repeated(dice,2) * 2
                if cls.filter_pips_repeated(dice, 2) else 0)

    @classmethod
    def two_pairs(cls, *dice):
        """
        utiliza una funcion que saca los numeros
        que se han repetido 2 veces y multiplica
        la suma por 2 si es que existen 2 parejas
        """
        return (sum(cls.filter_pips_repeated(dice, 2)) * 2
                if len(cls.filter_pips_repeated(dice, 2)) == 2 else 0)

    @classmethod
    def three_of_a_kind(cls, *dice):
        """
        si un numero se repite 3 veces se detecta 
        con la funcion filter pips repeated y si 
        exite ordena la lista y coje el numero del
        medio de la lista ordenada
        """
        return sorted(dice)[2] * 3 if cls.filter_pips_repeated(dice, 3) else 0

    @classmethod
    def four_of_a_kind(cls, *dice):
        """
        si un numero se repite 3 veces se detecta 
        con la funcion filter pips repeated y si 
        exite ordena la lista y coje el numero del
        medio de la lista ordenada
        """
        return sorted(dice)[2] * 4 if cls.filter_pips_repeated(dice, 4) else 0

    @classmethod
    def biggest_pip_repeated(cls, dice, times):
        """
        llama a la funcion filter_pips_repeated y 
        si devuelve algun numero coje el primero 
        (que es el mas alto) y lo devuelve
        """
        return (cls.filter_pips_repeated(dice, times)[0]
                if cls.filter_pips_repeated(dice, times) else [])

    @classmethod
    def filter_pips_repeated(cls, dice, times):
        """
        con el argumento times, numero de veces,
        crea una lista con los numeros que se 
        repites times veces ordenados de mayor a menor
        """
        return list(filter(lambda pip: dice.count(pip) >= times, [6,5,4,3,2,1]))

    @classmethod
    def small_straight(cls, *dice):
        """
        recibe una lista de enteros, los ordena
        y para que sume puntos con este sistema
        la lista ordenada tiene que ser los numeros
        de 1 al 5
        """
        return 15 if sorted(dice) == list(Pips.minus(Pips.SIX)) else 0

    @classmethod
    def large_straight(cls, *dice):
        """
        hace lo mismo que small_straight pero
        con los numeros del 2 al 6
        """
        return 20 if sorted(dice) == list(Pips.minus(Pips.ONE)) else 0

    @classmethod
    def full_house(cls, *dice):
        """
        para que puntue este metodo en la lista
        tienen que darnos un numero que aparezca
        2 veces y otro que aparezca 3,
        si se cumple la condicion se suman todos los numeros
        """
        return (sum(dice)
                if len(cls.filter_pips_repeated(dice, 2)) == 2
                and cls.filter_pips_repeated(dice, 3) else 0)
