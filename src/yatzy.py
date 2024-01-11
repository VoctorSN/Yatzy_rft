"""Modulo completo del ejercicio"""

from src.pips import Pips

class Yatzy:

    """Clase yatzy representa el juego yatzy
    con las funciones y constantes propias del juego"""

    MAX_POINTS = 50
    NO_POINTS = 0

    @staticmethod
    def only_repeated(dados:list,repeticiones:int) -> int:
        """devuelve una lista con los numeros repetidos 'repeticiones' veces"""
        return [dado for dado in set(dados) if dados.count(dado) >= repeticiones]

    @staticmethod
    def count_sum(dados:list,repeticiones:int,numero:int) -> int :
        """coge una lista (dados) y multiplica numero veces
        el numero repeticiones"""
        return dados.count(numero) * repeticiones

    @staticmethod
    def chance(*dados:list) -> int:
        """
        recibe varios parametros y suma todos ellos
        convertir los 5 argumentos en una lista mediante un *
        convirtiendolo en *args y asi poder usar la funcion sum
        """
        return sum(dados)

    @staticmethod
    def yatzy(*dados):
        """Genera una puntuacion de 50 en caso de que todos los
        dados de la tirada tengan el mismo valor y 0 en caso de
        que sean distinto valor"""
        return Yatzy.MAX_POINTS if len(set(dados)) == 1 else Yatzy.NO_POINTS

    @classmethod
    def ones(cls,*dados:list) -> int:
        return cls.count_sum(dados,1,Pips.ONE._value_)

    @classmethod
    def twos(cls,*dados:list) -> int:
        return cls.count_sum(dados,2,Pips.TWO._value_)

    @classmethod
    def threes(cls,*dados:list) -> int:
        return cls.count_sum(dados,3,Pips.THREE._value_)

    @classmethod
    def fours(cls,*dados:list) -> int:
        return cls.count_sum(dados,4,Pips.FOUR._value_)

    @classmethod
    def fives(cls,*dados:list) -> int:
        return cls.count_sum(dados,5,Pips.FIVE._value_)

    @classmethod
    def sixes(cls,*dados:list) -> int:
        return cls.count_sum(dados,6,Pips.SIX._value_)

    @classmethod
    def score_pair(cls,*dados:list) -> int:
        repetidos = cls.only_repeated(dados,2)
        return max(repetidos) * 2 if repetidos else Yatzy.NO_POINTS

    @classmethod
    def two_pair(cls,*dados:list) -> int:
        repetidos = cls.only_repeated(dados,2)
        return sum(repetidos) * 2 if len(repetidos) > 1 else Yatzy.NO_POINTS

    @classmethod
    def three_of_a_kind(cls,*dados:list) -> int:
        return sum(cls.only_repeated(dados,3)) * 3

    @classmethod
    def four_of_a_kind(cls,*dados) -> int:
        return sum(cls.only_repeated(dados,4)) * 4

    @classmethod
    def smallStraight(cls,*dados):
        return sum(dados) if sum(set(dados) - {Pips.SIX._value_}) == sum(dados) else Yatzy.NO_POINTS

    @classmethod
    def largeStraight(cls,*dados):
        return sum(dados) if sum(set(dados) - {Pips.ONE._value_}) == sum(dados) else Yatzy.NO_POINTS


    @classmethod
    def fullHouse(cls,*dados):
        return sum(dados) if len(cls.only_repeated(dados,2)) == 2 and len(set(dados)) == 2 else Yatzy.NO_POINTS
