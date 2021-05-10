from CentralBank import CentralBank
from agent.Agent import *

agents = []
runs = 40
central_bank = CentralBank()
agents_type = {
    "random": 1,
    "golden": 1
}


def setup():
    # for type in agents_type:
    agents.append(Random())


def run():
    for _ in range(runs):
        step()


def step():
    for a in agents:
        a.decide()
    central_bank.decide()


# -----------------------------------------------RUNNING_CODE-----------------------------------------------------------

# quando fazemos python.main.py é true, mas e fizermos apenas import main não é
if __name__ == "__main__":
    setup()
    run()
