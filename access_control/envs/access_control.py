import numpy as np
from collections import deque
import random
import gym
from gym import spaces

class AccessControlEnv(gym.Env):
    def __init__(self):

        self.n_servers = 10     # No. of servers
        self.priorities = [1, 2, 4, 8]  # List of possible priority scores for all customers
        self.n_priorities = len(self.priorities)
        self.free_prob = 0.06   # Probability of server freeing up

        self.observation_space = spaces.Tuple((spaces.Discrete(self.n_servers),
                                               spaces.Discrete(self.n_priorities)))
        self.action_space = spaces.Discrete(2)

        self.busy = None    # Queue containing all busy servers
        self.free = None    # Queue containing all free servers
        self.customer = None    # Priority of current customer
        self.state = None   # State of form [no. free servers, current customer priority]


    def step(self, action):

        if self.state is None:
            raise Exception("Please first initialize state using reset()")

        info = dict()

        # Free up any servers
        if len(self.busy) > 0:
            for _ in range(len(self.busy)):
                if random.random() <= self.free_prob:
                    self.free.append(self.busy.pop())

        if action == 0 or len(self.free) == 0:
            reward = 0
        elif action == 1 and len(self.free) > 0:
            reward = self.customer
            self.busy.append(self.free.pop())

        # Get next customer
        self.customer = random.choice(self.priorities)

        # Get next state
        self.state = np.array([len(self.free), self.customer])

        return self.state, reward, False, info


    def reset(self):
        self.customer = random.choice(self.priorities)
        self.busy = deque(maxlen=self.n_servers)
        self.free = deque([1] * self.n_servers, maxlen=self.n_servers)
        self.state = np.array([len(self.free), self.customer])
        return self.state

    def render(self, mode='human'):
        pass


