#!/usr/bin/env python

from brain_games.games import game_even
from brain_games.engine import game_go

def main():
    game_go(game_even)


if __name__ == '__main__':
    main()