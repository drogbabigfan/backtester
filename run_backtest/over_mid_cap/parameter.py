from backtest.parameter.momentum_parameters.momentum_parameters import MomentumParameters

class Parameter:
    def __init__(self):
        self.momentum_parameter = MomentumParameters()

    def get_parameter_dict(self):
        og_parameter_dict = self.momentum_parameter.get_parameter_dict()

