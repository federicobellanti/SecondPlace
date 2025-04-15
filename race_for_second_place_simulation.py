# Simulation for "Race for Second Place" - Version 2 (No Naives, One-Shot Game)

import numpy as np
import random
from collections import Counter
import pandas as pd

# Simulation Parameters
num_simulations = 1000
runners_per_race = 15
track_length = 1500  # meters
time_limit = 270  # seconds
dt = 0.5  # simulation time step in seconds

# Agent types included in core model
agent_types = ['Moderate', 'Intelligent', 'Unpredictable']
base_speeds = {
    'Moderate': (6.0, 0.3),
    'Intelligent': (6.2, 0.3),
    'Unpredictable': (6.1, 0.4)
}

# Initialize result counters
results = {
    'Wins': Counter(),
    'First Finisher': Counter(),
    'Prize Waived': 0
}

# Run simulations
for _ in range(num_simulations):
    agents = []
    types = random.choices(agent_types, k=runners_per_race)

    # Initialize runners
    for t in types:
        speed = np.random.normal(*base_speeds[t])
        agents.append({
            'type': t,
            'position': 0.0,
            'finished': False,
            'finish_time': None,
            'base_speed': speed
        })

    # Simulate race
    t = 0.0
    while t < time_limit:
        for agent in agents:
            if agent['finished']:
                continue

            pos = agent['position']
            agent_type = agent['type']
            others = [a for a in agents if a != agent]

            # Apply behavior logic
            if agent_type == 'Moderate':
                ahead = any(o['position'] > pos for o in others)
                speed = agent['base_speed'] - 0.2 if ahead else agent['base_speed']
            elif agent_type == 'Intelligent':
                too_close = any(0 < (o['position'] - pos) < 10 for o in others)
                speed = agent['base_speed'] - 0.3 if too_close else agent['base_speed']
            elif agent_type == 'Unpredictable':
                speed = agent['base_speed']
                if np.random.rand() < 0.1:
                    speed += np.random.uniform(-1.5, 1.5)
                if track_length - pos < 200:
                    speed += np.random.uniform(-1.0, 1.0)

            speed = max(0.1, speed)
            agent['position'] += speed * dt

            if agent['position'] >= track_length and not agent['finished']:
                agent['finished'] = True
                agent['finish_time'] = t

        t += dt

    finishers = [a for a in agents if a['finished']]
    finishers.sort(key=lambda x: x['finish_time'])

    if len(finishers) >= 2:
        results['First Finisher'][finishers[0]['type']] += 1
        results['Wins'][finishers[1]['type']] += 1
    else:
        results['Prize Waived'] += 1

# Summary results
expected_agents = runners_per_race * num_simulations / len(agent_types)
efficiency = {k: results['Wins'][k] / expected_agents for k in agent_types}

# Export results
summary_df = pd.DataFrame({
    'Agent Type': agent_types,
    'Wins': [results['Wins'][t] for t in agent_types],
    'Win Efficiency': [efficiency[t] for t in agent_types],
    'First Place Finishes': [results['First Finisher'][t] for t in agent_types]
})

summary_df.to_csv("simulation_results_scenario_b.csv", index=False)
