#!/usr/bin/env python

from brain_games.games import game_calc
from brain_games.engine import game_go

def main():
    game_go(game_calc)


if __name__ == '__main__':
    main()