import math

itens = int(input('Enter the number of items: '))
itens_box = int(input('Enter the number of items per box: '))

boxes = math.ceil(itens/itens_box)

print(f'For {itens} itens, packing {itens_box} in each box, you will need {boxes} boxes')