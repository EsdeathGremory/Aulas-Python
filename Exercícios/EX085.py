import random


class JoKenPo:
    def __init__(self):
        self.__pc = random.randint(1, 3)

    @property
    def pc(self):
        return self.__pc

    @pc.setter
    def pc(self, mao):
        if mao == 1 and self.__pc == 3:
            print("Victory")
        elif mao == 2 and self.__pc == 1:
            print("Victory")
        elif mao == 3 and self.__pc == 2:
            print("Victory")
        elif mao == self.__pc:
            print("Draw")
        else:
            print("Defeat")


jogo = int(input("------ Jo - Ken - Po ------\n[1] - Pedra\n[2] - Papel\n[3] - Tesoura\n-->"))

jokenpo = JoKenPo()

jokenpo.pc = jogo
