import random
pontos_seus = 0
pontos_deles = 0
while(True):
  cor_secreta = random.choice(['R', 'G', 'B'])
  print(cor_secreta)
  palpite = input("Adivinhe a cor (R, G, B): ").upper()
  if palpite not in ['R', 'G', 'B']:
    print("Entrada inválida. Escolha R, G ou B.")
  elif palpite == cor_secreta:
    print("Parabéns! Acertou! ^^")
    pontos_seus = pontos_seus + 1
  else:
    print("Puts...")
    pontos_deles = pontos_deles + 1
  print('A cor era ', cor_secreta)
  print(f'Você {pontos_seus} VS Compiuter {pontos_deles}')