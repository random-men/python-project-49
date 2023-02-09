#!/usr/bin/env python

from brain_games.games import game_gcd
from brain_games.engine import game_go

def main():
    game_go(game_gcd)


if __name__ == '__main__':
    main()