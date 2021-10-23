#!/usr/bin/env

from brain_games.cli import welcome_user
from brain_games.brain_even import check_even

def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    check_even(name)

if __name__ == '__main__':
    main()
