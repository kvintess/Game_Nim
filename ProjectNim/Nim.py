#It's an easy mathematic game named Nim

from Nim_engine import put_stones, take_from_bunch, get_bunches, is_gameover
from termcolor import cprint, colored
put_stones()
user_number = 1
while True:
    cprint('Текущая позиция', 'red')
    print(get_bunches())
    color_of_player = 'green' if user_number==1 else 'yellow'
    cprint('ходит игрок {}'.format(user_number), color_of_player)
    pos=int(input(colored(('Откуда берем?'), color_of_player)))
    qua=int(input('Сколько берем?'))
    step_successed = take_from_bunch(position=pos, quantity=qua)
    if step_successed:
        user_number = 2 if user_number == 1 else 1
    else:
        cprint('Какая-то ошибка', 'yellow')
    if is_gameover():
        break

print('победа игрока номер ', user_number)
