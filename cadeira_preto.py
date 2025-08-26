#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
# ----------------------------------------------------------------------------
# Created By  : Joás   Line 3
# Created Date: 25/08/2025
# version ='1.0'
# ---------------------------------------------------------------------------
"""Isso é um cabeçalho, um cabeçalho é um bloco de comentários na parte superior do código, 
que inclui o nome do arquivo, autor, data e alguns outros detalhes do arquivo e o conteúdo 
desse arquivo. Seguem-se módulos embutidos importados e importações de terceiros. """  # Line 4
# ---------------------------------------------------------------------------
# Imports Line 5
# ---------------------------------------------------------------------------
from ... import ...  # Line 6
# ---------------------------------------------------------------------------
'''Uma docstring é um comentário explicando uma função ou parametros mais complexos
onde um comentãrio simples é guardado para explicações menores, cabeçalhos contém as 
docstrings de um projeto e pode ser feita de diferentes maneiras dependendo do desenvolvefor''' # Line7



######################################################################

# implemente as funções abaixo e coloque as docstrings

def maximo(nums):
    """oque faz
    oque recebe
    oque retorna"""
    # TODO: percorra a lista guardando o maior atual
    ...

def e_par(n: int) -> bool:
    """ ... """
    # TODO: retorne se n é par
    ...
def fatorial(n: int) -> int:
    """   ...  """
    # TODO: implemente de forma iterativa (sem recursão)
    ...
import re

def limpa_texto(s: str) -> str:
    """..."""
    # TODO: converta s para minúsculo e remova pontuações como ,.;:!?'"()-_
    ...

def conta_vogais(s: str) -> int:
    """....."""
    # TODO: conte as vogais simples
    ...

def palindromo(s: str) -> bool:
    """..."""
    # TODO: normalizar (minúsculo, remover não alfanumérico) e comparar com o reverso
    ...

def total_por_vendedor(vendas):
    """
    executa......
    Recebe: lista de tuplas (nome, valor).
    Retorna: dict {nome: soma_valores}
    """
    # TODO: inicialize um dict e vá somando
    ...

def melhor_vendedor(totais: dict):
    """
    ...
    Recebe ...
    Retorna (nome, total) com o maior total.
    Se dict vazio, levante ValueError.
    """
    # TODO: encontre o par com maior total (sem ordenar a lista inteira)
    ...
