#It's an easy mathematic game named Nim
#it's my token, i'm afraid to forget it
# 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
from Nim_engine import put_stones, take_from_bunch, get_bunches, is_gameover
put_stones()
while True:
    print('Текущая позиция')
    print(get_bunches())
    pos=int(input('Откуда берем?'))
    qua=int(input('Сколько берем?'))
    take_from_bunch(position=pos, quantity=qua)
    print(len(Nim_engine._holder))



    if is_gameover():
        break
