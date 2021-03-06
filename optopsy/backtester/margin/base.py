from abc import ABC, abstractmethod


class AbstractOptionMargin(ABC):

    def __init__(self):
        pass

    @staticmethod
    def parse_exp_strikes(exp, strikes):
        # split the labels by slash as it may contain more than one item
        strikes = strikes.split("/")
        exps = exp.split("/")
        return exps, strikes

    @abstractmethod
    def single(self, cost_of_trade, action, strikes, exp_label):
        raise NotImplementedError("Should implement single()")

    @abstractmethod
    def vertical(self, cost_of_trade, action, strikes, exp_label):
        raise NotImplementedError("Should implement vertical()")

    @abstractmethod
    def iron_condor(self, cost_of_trade, action, strikes, exp_label):
        raise NotImplementedError("Should implement iron_condor()")

    @abstractmethod
    def covered_stock(self, cost_of_trade, action, strikes, exp_label):
        raise NotImplementedError("Should implement covered_stock()")

    @abstractmethod
    def diagonal(self, cost_of_trade, action, strikes, exp_label):
        raise NotImplementedError("Should implement diagonal()")

    @abstractmethod
    def double_diagonal(self, cost_of_trade, action, strikes, exp_label):
        raise NotImplementedError("Should implement double_diagonal()")

    @abstractmethod
    def calendar(self, cost_of_trade, action, strikes, exp_label):
        raise NotImplementedError("Should implement calendar()")

    @abstractmethod
    def straddle(self, cost_of_trade, action, strikes, exp_label):
        raise NotImplementedError("Should implement straddle()")

    @abstractmethod
    def strangle(self, cost_of_trade, action, strikes, exp_label):
        raise NotImplementedError("Should implement strangle()")

    @abstractmethod
    def combo(self, cost_of_trade, action, strikes, exp_label):
        raise NotImplementedError("Should implement combo()")

    @abstractmethod
    def back_ratio(self, cost_of_trade, action, strikes, exp_label):
        raise NotImplementedError("Should implement back_ratio()")

    @abstractmethod
    def butterfly(self, cost_of_trade, action, strikes, exp_label):
        raise NotImplementedError("Should implement butterfly()")
