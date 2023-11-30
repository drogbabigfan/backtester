from typing import Optional
import bt
from backtest.bt.operation_types import Operation
from backtest.bt.rebalance_condition import RebalanceCondition


class RebalanceOnCondition(bt.Algo):
    def __init__(self, condition_instance: RebalanceCondition, operation: Optional[Operation] = None):
        self.condition_instance = condition_instance
        self.operation = operation

    def __call__(self, target: bt.AlgoStack) -> bool:
        current_date = target.now
        if self.operation:
            return self.condition_instance.check_rebalance_condition(current_date, self.operation)