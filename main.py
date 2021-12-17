from termcolor import colored
from PIL import Image


""" image open upon winning """
winner_image = Image.open('winner.jpeg')

""" list where each element maps to a grid section """
sections = [0,1,2,3,4,5,6,7,8]


""" game template with replaceable values in each seciton (1-9) """
def ready_template() -> None:
    print('     |     |     ')
    print(f'  {sections[0]}  |  {sections[1]}  |  {sections[2]}   ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {sections[3]}  |  {sections[4]}  |  {sections[5]}   ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {sections[6]}  |  {sections[7]}  |  {sections[8]}   ')
    print('     |     |     ')
    return None



""" check lines for 3 consecutive symbols of the same type """
def check_lines():
    # top row
    if sections[0] == sections[1] == sections[2]:
        print(colored('WINNER!', 'red' ,on_color='on_white', attrs=['bold']))
        return True
    # middle row
    if sections[3] == sections[4] == sections[5]:
        print(colored('WINNER!', 'red' ,on_color='on_white', attrs=['bold']))
        return True
    # bottom row
    if sections[6] == sections[7] == sections[8]:
        print(colored('WINNER!', 'red' ,on_color='on_white', attrs=['bold']))
        return True
    # left col
    if sections[0] == sections[3] == sections[6]:
        print(colored('WINNER!', 'red' ,on_color='on_white', attrs=['bold']))
        return True
    # mid col
    if sections[1] == sections[4] == sections[7]:
        print(colored('WINNER!', 'red' ,on_color='on_white', attrs=['bold']))
        return True
    # right col
    if sections[2] == sections[5] == sections[8]:
        print(colored('WINNER!', 'red' ,on_color='on_white', attrs=['bold']))
        return True
    # diagonal 1
    if sections[0] == sections[4] == sections[8]:
        print(colored('WINNER!', 'red' ,on_color='on_white', attrs=['bold']))
        return True
    # diagonal 2
    if sections[2] == sections[4] == sections[6]:
        print(colored('WINNER!', 'red' ,on_color='on_white', attrs=['bold']))
        return True


def play_game() -> None:
    turn_count = 1
    while True:

        ready_template()
        if check_lines() == True:
                break
        user_input = int(input('Place symbol in section: ')) # Change symbol to either X or O based on turn

        # placing user input in list
        if user_input in sections:
            sections.pop(user_input)
            if turn_count%2 == 0: # setting O's to player 2 (even turn count)
                value_O = colored('O','red', attrs=['bold'])
                sections.insert(user_input, value_O)
            else:
                global value_X
                value_X = colored('X','magenta', attrs=['bold'])
                sections.insert(user_input, value_X)
        turn_count = turn_count + 1 
    winner_image.show()


play_game()
