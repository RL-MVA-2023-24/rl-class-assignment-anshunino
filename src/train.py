from gymnasium.wrappers import TimeLimit
from env_hiv import HIVPatient
import numpy as np
import torch.nn as nn
import torch

env = TimeLimit(
    env=HIVPatient(domain_randomization=False), max_episode_steps=200
)  # The time wrapper limits the number of steps in an episode at 200.
# Now is the floor is yours to implement the agent and train it.


# You have to implement your own agent.
# Don't modify the methods names and signatures, but you can add methods.
# ENJOY!
class ProjectAgent:
    def __init__(self):
        hidden_size = 512
        self.best_model = torch.nn.Sequential(nn.Linear(6, hidden_size),
                          nn.ReLU(),
                          nn.Linear(hidden_size, hidden_size),
                          nn.ReLU(),
                          nn.Linear(hidden_size, 4))

    def act(self, observation, use_random=False):
        Q_func = self.best_model(torch.Tensor(observation).unsqueeze(0))
        return torch.argmax(Q_func).item()

    def save(self, path):
        pass

    def load(self):
        # load best model state dict from pickle
        import pickle
        with open('model_3_layer_512.pkl', 'rb') as f:
            best_model_state_dict = pickle.load(f)
            #self.best_model = pickle.load(f)

        #self.best_model.to(device=torch.device('cpu'))
        self.best_model.load_state_dict(best_model_state_dict)
