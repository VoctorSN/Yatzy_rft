"""Modulo completo del ejercicio"""

from typing import List
from src.pips import Pips

class Yatzy:

    """Clase yatzy representa el juego yatzy
    con las funciones y constantes propias del juego"""

    MAX_PUNTOS = 50
    MIN_PUNTOS = 0
    dice_list = List[int]

    @staticmethod
    def __solo_repetidos(dados:list[int],repeticiones:int) -> list[int]:
        """devuelve una lista con los numeros repetidos 'repeticiones' veces, 
        es una funcion privada y solo la uso dentro de la clase"""
        return list(filter(lambda dado: dados.count(dado)>= repeticiones,set(dados)))

    @staticmethod
    def __contar_sumar(dados:dice_list,numero:int) -> int :
        """coge una lista (dados) y multiplica 'numero' veces
        por numero, es una funcion privada y solo
        la uso dentro de la clase"""
        return dados.count(numero) * numero

    @staticmethod
    def chance(*dados:dice_list) -> int:
        """
        recibe varios parametros y suma todos ellos
        convertir los Pips.FIVE.value argumentos en una lista mediante un *
        convirtiendolo en *args y asi poder usar la funcion sum
        
        """
        return sum(dados)

    @staticmethod
    def yatzy(*dados:dice_list) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        return Yatzy.MAX_PUNTOS if len(set(dados)) == Pips.UNO.value else Yatzy.MIN_PUNTOS

    @classmethod
    def ones(cls,*dados:dice_list) -> int:
        return cls.__contar_sumar(dados,Pips.UNO.value)

    @classmethod
    def DOSs(cls,*dados:dice_list) -> int:
        return cls.__contar_sumar(dados,Pips.DOS.value)

    @classmethod
    def threes(cls,*dados:dice_list) -> int:
        return cls.__contar_sumar(dados,Pips.TRES.value)

    @classmethod
    def fours(cls,*dados:dice_list) -> int:
        return cls.__contar_sumar(dados,Pips.CUATRO.value)

    @classmethod
    def fives(cls,*dados:dice_list) -> int:
        return cls.__contar_sumar(dados,Pips.CINCO.value)

    @classmethod
    def SEISes(cls,*dados:dice_list) -> int:
        return cls.__contar_sumar(dados,Pips.SEIS.value)

    @classmethod
    def score_pair(cls,*dados:dice_list) -> int:
        repetidos = cls.__solo_repetidos(dados,Pips.DOS.value)
        return max(repetidos) * Pips.DOS.value if repetidos else Yatzy.MIN_PUNTOS

    @classmethod
    def DOS_pair(cls,*dados:list[int]) -> int:
        """Usa la funcion __solo_repetidos que nos indica el numero que se repite una cantidad exacta de veces, en este caso Pips.DOS.value y lo multiplica por dos para obtener la puntuación"""
        repetidos = cls.__solo_repetidos(dados,Pips.DOS.value)
        return sum(repetidos) * Pips.DOS.value if len(repetidos) == Pips.DOS.value else Yatzy.MIN_PUNTOS

    @classmethod
    def three_of_a_kind(cls,*dados:list[int]) -> int:
        return sum(cls.__solo_repetidos(dados,Pips.TRES.value)) * Pips.TRES.value

    @classmethod
    def four_of_a_kind(cls,*dados:list[int]) -> int:
        return sum(cls.__solo_repetidos(dados,Pips.CUATRO.value)) * Pips.CUATRO.value

    @classmethod
    def smallStraight(cls,*dados:list[int]) -> int:
        return sum(dados) if sum(set(dados) - {Pips.SEIS.value}) == sum(dados) else Yatzy.MIN_PUNTOS

    @classmethod
    def largeStraight(cls,*dados:list[int]) -> int:
        return sum(dados) if sum(set(dados) - {Pips.UNO.value}) == sum(dados) else Yatzy.MIN_PUNTOS


    @classmethod
    def fullHouse(cls,*dados:list[int]) -> int:
        return sum(dados) if len(cls.__solo_repetidos(dados,Pips.DOS.value)) == Pips.DOS.value and len(set(dados)) == Pips.DOS.value else Yatzy.MIN_PUNTOS
