from typing import List, Callable
from simple_hand import (deal, new_hand, up_card, add_card, total)

def stop_at_17(hand: List[int], opponent_up_card: int) -> bool:
    return total(hand) < 17

def test_strategies(player_strategy: Callable,
                    house_strategy: Callable,
                    num_games: int) -> float:
    pass

def play_hand(strategy: Callable, hand: List[int], opponent_up_card: int) -> List[int]:
    if total(hand) > 21:
        return hand
    if strategy(hand, opponent_up_card):  # Should I hit?
        return play_hand(strategy, add_card(hand, deal()), opponent_up_card)
    else:
        return hand

def play_game(player_strategy: Callable, house_strategy: Callable) -> int:
    house_initial_hand = new_hand()
    player_hand = play_hand(player_strategy, new_hand(), up_card(house_initial_hand))
    if total(player_hand) > 21:
        return 0
    
    house_hand = play_hand(house_strategy, house_initial_hand, up_card(player_hand))

    if total(house_hand) > 21:
        return 1   # House bust
    
    if total(player_hand) > total(house_hand):
        return 1   # House lost
    else:
        return 0   # Player lost