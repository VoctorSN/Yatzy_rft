"""Modulo completo del ejercicio"""

from src.pips import Pips

class Yatzy:

    """Clase yatzy representa el juego yatzy
    con las funciones y constantes propias del juego"""

    MAX_POINTS = 50
    NO_POINTS = 0

    @staticmethod
    def __only_repeated(dados:list[int],repeticiones:int) -> list[int]:
        """devuelve una lista con los numeros repetidos 'repeticiones' veces"""
        return [dado for dado in set(dados) if dados.count(dado) >= repeticiones]

    @staticmethod
    def __count_sum(dados:list[int],numero:int) -> int :
        """coge una lista (dados) y multiplica numero veces
        el numero repeticiones, es una funcion privada y solo
        la uso dentro de la clase"""
        return dados.count(numero) * numero

    @staticmethod
    def chance(*dados:list[int]) -> int:
        """
        recibe varios parametros y suma todos ellos
        convertir los Pips.FIVE.value argumentos en una lista mediante un *
        convirtiendolo en *args y asi poder usar la funcion sum
        , es una funcion privada y solo la uso dentro de la clase
        """
        return sum(dados)

    @staticmethod
    def yatzy(*dados:list[int]):
        return Yatzy.MAX_POINTS if len(set(dados)) == Pips.ONE.value else Yatzy.NO_POINTS

    @classmethod
    def ones(cls,*dados:list[int]) -> int:
        return cls.__count_sum(dados,Pips.ONE.value)

    @classmethod
    def twos(cls,*dados:list[int]) -> int:
        return cls.__count_sum(dados,Pips.TWO.value)

    @classmethod
    def threes(cls,*dados:list[int]) -> int:
        return cls.__count_sum(dados,Pips.THREE.value)

    @classmethod
    def fours(cls,*dados:list[int]) -> int:
        return cls.__count_sum(dados,Pips.FOUR.value)

    @classmethod
    def fives(cls,*dados:list[int]) -> int:
        return cls.__count_sum(dados,Pips.FIVE.value)

    @classmethod
    def sixes(cls,*dados:list[int]) -> int:
        return cls.__count_sum(dados,Pips.SIX.value)

    @classmethod
    def score_pair(cls,*dados:list[int]) -> int:
        maximo_repetido=cls.__only_repeated(dados,Pips.TWO.value)
        return max(maximo_repetido) * Pips.TWO.value if maximo_repetido else Yatzy.NO_POINTS

    @classmethod
    def two_pair(cls,*dados:list[int]) -> int:
        """Usa la funcion __only_repeated que nos indica el numero que se repite una cantidad exacta de veces, en este caso Pips.TWO.value y lo multiplica por dos para obtener la puntuación"""
        repetidos = cls.__only_repeated(dados,Pips.TWO.value)
        return sum(repetidos) * Pips.TWO.value if len(repetidos) == Pips.TWO.value else Yatzy.NO_POINTS

    @classmethod
    def three_of_a_kind(cls,*dados:list[int]) -> int:
        return sum(cls.__only_repeated(dados,Pips.THREE.value)) * Pips.THREE.value

    @classmethod
    def four_of_a_kind(cls,*dados:list[int]) -> int:
        return sum(cls.__only_repeated(dados,Pips.FOUR.value)) * Pips.FOUR.value

    @classmethod
    def smallStraight(cls,*dados:list[int]) -> int:
        return sum(dados) if sum(set(dados) - {Pips.SIX.value}) == sum(dados) else Yatzy.NO_POINTS

    @classmethod
    def largeStraight(cls,*dados:list[int]) -> int:
        return sum(dados) if sum(set(dados) - {Pips.ONE.value}) == sum(dados) else Yatzy.NO_POINTS


    @classmethod
    def fullHouse(cls,*dados:list[int]) -> int:
        return sum(dados) if len(cls.__only_repeated(dados,Pips.TWO.value)) == Pips.TWO.value and len(set(dados)) == Pips.TWO.value else Yatzy.NO_POINTS
