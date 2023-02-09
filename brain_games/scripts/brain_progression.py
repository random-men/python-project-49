#!/usr/bin/env python

from brain_games.games import game_progression
from brain_games.engine import game_go

def main():
    game_go(game_progression)


if __name__ == '__main__':
    main()