from __future__ import annotations
from abc import ABC, abstractmethod
import random
class Context():

    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def check_cup(self):
        print(f"Checking cup {self._strategy.name}:")
        print(self._strategy.do_algorithm())


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self):
        pass
    

class CupA(Strategy):
    name = 'Cup 1'
    ball_there = False

    @property
    def ball(self):
        return self.ball_there

    @ball.setter
    def ball(self, ball):
        self.ball_there = ball

    def do_algorithm(self):
        if self.ball == True:
            return f"The ball is here!"
        else:
            return f"The ball isn't here!"

class CupB(Strategy):
    name = 'Cup 2'
    ball_there = False

    @property
    def ball(self):
        return self.ball_there

    @ball.setter
    def ball(self, ball):
        self.ball_there = ball

    def do_algorithm(self):
        if self.ball == True:
            return f"The ball is here!"
        else:
            return f"The ball isn't here!"

class CupC(Strategy):
    name = 'Cup 3'
    ball_there = False

    @property
    def ball(self):
        return self.ball_there

    @ball.setter
    def ball(self, ball):
        self.ball_there = ball

    def do_algorithm(self):
        if self.ball == True:
            return f"The ball is here!"
        else:
            return f"The ball isn't here!"


if __name__ == "__main__":
    cups = [CupA(), CupB(), CupC()]
    random.choice(cups).ball = True

    context = Context(cups[0])
    print(f"Player choose {context._strategy.name}:")
    context.check_cup()
    print()
    context.strategy = cups[2]
    print(f"Player choose {context._strategy.name}:")
    context.check_cup()