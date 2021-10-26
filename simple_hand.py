"""
Simplified version of blackjack.
Based on https://github.com/SICPDistilled/blackjack
"""
from random import randint
from typing import List
from functools import reduce
from operator import add


def deal()->int:
    return randint(1, 10)

def new_hand()->List[int]:
    return [deal()]

def up_card(hand):
    return hand[0]

def add_card(hand, card):
    return hand + [card]

def total(hand):
    return reduce(add, hand)
