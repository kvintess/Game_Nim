#It's an easy mathematic game named Nim
from Nim_engine import put_stones, take_from_bunch, get_bunches, is_gameover
put_stones()
while True:
    print('Текущая позиция')
    print(get_bunches())
    pos=input('Откуда берем?')
    qua=input('Сколько берем?')
    take_from_bunch(position=pos, quontity=qua)
    if is_gameover():
        break
