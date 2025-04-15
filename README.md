# The Race for Second Place — Simulation Code

This repository contains the simulation code accompanying the academic manuscript:

**"The Race for Second Place: A Game-Theoretic Model of Reverse Incentives and Adaptive Strategy Under Observability and Time Pressure"**  
Author: Federico Bellanti  
Date: April 2025  
[LinkedIn / Website / Contact — optional]

--------------------

## 📘 Overview

This Python script simulates a novel one-shot game in which the objective is not to finish first, but **second**. The game models a 1500m race involving heterogeneous agents with varying levels of strategic reasoning and randomness. Agents observe each other in real time but cannot communicate, and the race ends after a fixed time limit.

The model explores how different agent types — **Intelligent**, **Moderate**, and **Unpredictable** — perform under these constraints, and whether intelligent strategies are sufficient to win in a chaotic environment.

--------------------

## 📂 Contents

- `race_for_second_place_simulation.py`: Main simulation script
- `simulation_results_scenario_b.csv`: Example output data (optional)
- `figures/`: Folder for output charts (optional)
- `LICENSE`: (optional — e.g., MIT)

--------------------

## ⚙️ Requirements

This project uses Python 3.x and the following libraries:

```bash
numpy
pandas
matplotlib

--------------------

## ⚙️ Install dependencies using pip:

pip install numpy pandas matplotlib

--------------------

## ▶️ How to Run

To simulate 1,000 races and export results to CSV:
python race_for_second_place_simulation.py

The script will:

Randomly generate agents

Simulate race dynamics

Record first- and second-place results

Output a results table (optional CSV)

--------------------

## 📊 Output

The simulation outputs:

Win frequency by agent type

Win efficiency (wins per expected agent)

First-place finisher distribution

These data can be used to replicate the figures in the associated academic paper.

--------------------

## 📖 Citation

If you use this code in your own research, please cite:

Bellanti, F. (2025). Simulation code for “The Race for Second Place.” GitHub repository: https://github.com/federicobellanti/SecondPlace

--------------------

## 📄 License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).  
See the [LICENSE](./LICENSE) file for details.

--------------------

## 🧠 Acknowledgments

Thanks to the behavioral game theory and agent-based modeling community for foundational concepts. 
This project was developed as part of an original research effort in strategic coordination under reverse incentives.
