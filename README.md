# AASMA Project: Wall Street Bets: The Game

#### Autonomous Agents and Multi-Agent Systems Course
#### A Competitive Multi-Agent Approach

2020/2021

Group number

| Name               | Number |
| -----------------  | ------ |
| Carolina Carreira  | 87641  |
| João Olival        | 94111  |
| Sebastião Almeida  | 97115  |

## Project Description

The stock market is a systems where multiple agents interact.
This has inspired us to implement this fun game to educate users to learn more about the economy. Each agent is an investor and agents can have different strategies (based on real life examples) and their goal is to maximize their value. By testing the developed system we learned more about the agent's interactions and how different strategies perform against each other.

## Features

- A customizable set of agents whose goal is to maximize their total value (cash plus total share value) over time. 
- Discrete time, for simplicity, and all agents have the opportunity to buy and/or sell stocks at each time step. 
- Number of steps of each run is also be customizable. 
- The price of the stocks takes into account the normal rules of supply and demand. 
- There are some realistic events that can happen throughout the simulation and influence the price of the stocks, though the option to disable them will also be present. 
- There is a variety of stocks with diferent relations between them, for example, complementary and competitive companies.


## How to run

### Requirements:

- Python 3.8 
- PyGame 2.0.1 (`pip install pygame`)
- Matplotlib (`pip install matplotlib`)

### To run:

`
python3 main.py
` 


### Settings:

To navigate the interface you can use the arrow keys. To select an option press enter. To return to the previous menu press return. To advance a step press the right arrow key. To know information abou each agent hover above their name.

In the menu "Options" you can change all the settings of the app regarding:
- Agents' type
- Number of agents (maximum is 8 in total)
- Steps per game
- Game mode (Default, Inflation and Recession)




This code is written according to [PEP 8 -- Style](https://www.python.org/dev/peps/pep-0008/).
