class Character:
    def __init__(
            self,
            name: str,
            health: int,
            stamina: int,
            strength: int,
            dexterity: int,
            resilience: int,
            intellect: int,
    ):
        self.name = name
        self.health = health
        self.stamina = stamina
        self._strength = strength
        self._dexterity = dexterity
        self._resilience = resilience
        self._intellect = intellect
        self.__main_attrs: dict[str, int]
        self.__secondary_attrs: dict[str, int]
        self.perks = []


class Hero(Character):
    def __init__(
            self,
            name: str,
            level: int,
            health: int,
            stamina: int,
            strength: int,
            dexterity: int,
            resilience: int,
            intellect: int,
    ):
        super().__init__(
            name,
            health,
            stamina,
            strength,
            dexterity,
            resilience,
            intellect
        )
        self.level = level

    def level_up(self):
        self.level += 1
        self.health += 10 * (self._strength / 50 - 1)


class NPC(Character):
    def __init__(
            self,
            name: str,
            health: int,
            stamina: int,
            strength: int,
            dexterity: int,
            resilience: int,
            intellect: int,
    ):
        super().__init__(
            name,
            health,
            stamina,
            strength,
            dexterity,
            resilience,
            intellect
        )
        self.health = 10**6


class Mob(Character):
    def _scale(self, level: int):
        coeff = level * self.health / 100
        self._strength *= coeff
        self._dexterity *= coeff
        self._resilience *= coeff
        self._intellect *= coeff


class Fighter(Hero):
    def __init__(
            self,
            name: str,
            level: int,
            health: int,
            stamina: int,
            fury: int,
            strength: int,
            dexterity: int,
            resilience: int,
            intellect: int,
    ):
        super().__init__(
            name,
            health,
            level,
            stamina,
            strength,
            dexterity,
            resilience,
            intellect
        )
        self.fury = fury
