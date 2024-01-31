from simulator.simulator import Simulator
from planner import Planner
from policy import *
from task_execution_time import ExecutionTimeModel

prediction_model = ExecutionTimeModel()
warm_up_policy = RandomPolicy()
warm_up_time =  24
#policy = RandomPolicy()
policy = HungarianPolicy()
policy = GreedyParallelMachinesSchedulingPolicy()
my_planner = Planner(prediction_model, warm_up_policy, warm_up_time, policy,
                     predict_multiple=True)

simulator = Simulator(my_planner)
result = simulator.run(2*24*365)
print(result)