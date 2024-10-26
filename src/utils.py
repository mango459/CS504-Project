"""This is a place for re-usable functions that can be helpful anywhere in the code. Don't put stuff
that's really specific in here but just general tools that you may or may not use elsewhere."""
import os
import itertools

def get_bool_input(prompt:str) -> bool:
    """Validates yes no q's into bools"""
    usr_input = ''
    counter = itertools.count()
    valid_inputs = ('yes', 'no', 'y', 'n')
    while not usr_input in valid_inputs:
        if next(counter) > 0:
            print(f'Please provide valid input: {valid_inputs} ')
        usr_input = input(f"{prompt} [y/n] ").lower()
    mapper = dict(yes=True, y=True, no=False, n=False)
    return mapper.get(usr_input)

def get_filepath(prompt:str) -> str:
    """Validates a filepath input from the user"""
    usr_input = ''
    counter = itertools.count()
    while not os.path.isdir(usr_input):
        if next(counter) > 0:
            print(f"{usr_input} is not a valid directory")
        usr_input = input(f"{prompt} ")
    return usr_input