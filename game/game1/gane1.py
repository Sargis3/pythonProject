class Game:
    __xp_give = 0
    __xp_lose = 40

    def get_xp(self):
        return self.__xp_give

    def lose_xp(self):
        return self.__xp_lose
