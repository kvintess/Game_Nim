#It's an easy mathematic game named Nim

from Nim_engine import put_stones, take_from_bunch, get_bunches, is_gameover
from termcolor import cprint
put_stones()
user_number = 1
while True:
    cprint('Текущая позиция', 'red')
    print(get_bunches())
    color_of_player = 'yellow' if user_number==1 else 'green'
    cprint('ходит игрок {}'.format(user_number), color_of_player)
    pos=int(input('Откуда берем?'))
    qua=int(input('Сколько берем?'))
    take_from_bunch(position=pos, quantity=qua)
    if is_gameover():
        break
    user_number = 2 if user_number == 1 else 1
print('победа игрока номер ', user_number)
