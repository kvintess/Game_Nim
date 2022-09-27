#It's an easy mathematic game named Nim
#it's my token, i'm afraid to forget it
# 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
from Nim_engine import put_stones, take_from_bunch, get_bunches, is_gameover
put_stones()
user_number = 1
while True:
    print('Текущая позиция')
    print(get_bunches())
    print('ходит игрок {}'.format(user_number))
    pos=int(input('Откуда берем?'))
    qua=int(input('Сколько берем?'))
    take_from_bunch(position=pos, quantity=qua)
    if is_gameover():
        break
    user_number = 2 if user_number == 1 else 1
print('победа игрока номер ', user_number)
