class Personagem:
    def __init__(self, nome):
        self._nome = nome.strip().capitalize()
        self._vida = 100
        self._experiencia = 0
        self._nivel = 1

    @property
    def nome(self):
        return f"PERSONAGEM: {self._nome}"

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.strip().capitalize()

    @property
    def vida(self):
        return f"VIDA: {self._vida}"

    @property
    def experiencia(self):
        return f"XP: {self._experiencia}"

    @property
    def nivel(self):
        return f"NIVEL: {self._nivel}"


class Mage(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.__power = None
        self.staff = "Pau"

    def __str__(self):
        return (f"---- Mage ----\n"
                f"NOME: {self._nome}\n"
                f"PONTOS VITAIS: {self._vida}\n"
                f"XP: {self._experiencia}\n"
                f"NIVEL: {self._nivel}\n"
                f"POWER: {self.__power}\n"
                f"STAFF: {self.staff}")

    @property
    def power(self):
        return f"Nenhum poder disponivel" if self.__power is None else f"PODER: {self.__power}"

    @power.setter
    def power(self, novo_poder):
        self.__power = novo_poder
