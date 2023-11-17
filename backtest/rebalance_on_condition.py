import bt
from typing import Optional
from backtest.rebalance_condition import RebalanceCondition

## TODO: TEST 필요
class RebalanceOnCondition(bt.Algo):
    def __init__(self, condition_instance: RebalanceCondition, operation: Optional[str] = None):
        self.condition_instance = condition_instance
        self.operation = operation

    def __call__(self, target: bt.AlgoStack) -> bool:
        current_date = target.now
        if self.operation:
            return self.condition_instance.check_rebalance_condition(current_date, self.operation)