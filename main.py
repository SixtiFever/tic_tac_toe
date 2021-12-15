

sections = [0,1,2,3,4,5,6,7,8]
turn_count = 1

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

def place_symbol() -> None:
    while True:
        turn_count = turn_count + 1
        ready_template()
        user_input = int(input('Place symbol in section: ')) # Change symbol to either X or O based on turn
        if user_input in sections:
            sections.pop(user_input)
            sections.insert(user_input, 'X')
        return None



place_symbol()