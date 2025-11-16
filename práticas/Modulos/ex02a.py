import random

num = random.randint(1,10)

print(num)

import emoji

print(emoji.emojize("Olá :OK_hand:"))


# Mostra todos os aliases disponíveis (nomes dos emojis)
for nome, simbolo in emoji.EMOJI_DATA.items():
    print(f"{nome} -> {simbolo['en']}")
