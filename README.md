An implementation of the Access-Control Queuing task 
from Example 10.2 of [(Sutton and Barto, 2018)](http://www.incompleteideas.net/book/RLbook2020.pdf)
using the OpenAI Gym API [(Brockwell et al., 2016)](http://arxiv.org/abs/1606.01540).

#### Description of Environment (from [(Sutton and Barto, 2018)](http://www.incompleteideas.net/book/RLbook2020.pdf)):

This is a decision task involving
access control to a set of 10 servers. Customers of four different priorities arrive at a
single queue. If given access to a server, the customers pay a reward of 1, 2, 4, or 8 to
the server, depending on their priority, with higher priority customers paying more. In
each time step, the customer at the head of the queue is either accepted (assigned to one
of the servers) or rejected (removed from the queue, with a reward of zero). In either
case, on the next time step the next customer in the queue is considered. The queue
never empties, and the priorities of the customers in the queue are equally randomly
distributed. Of course a customer cannot be served if there is no free server; the customer
is always rejected in this case. Each busy server becomes free with probability p = 0.06
on each time step. Although we have just described them for definiteness, let us assume
the statistics of arrivals and departures are unknown. The task is to decide on each step
whether to accept or reject the next customer, on the basis of his priority and the number
of free servers, so as to maximize long-term reward without discounting.

#### Requirements
* ```python 3``` (tested on 3.8.3)
* ```gym``` (tested on 0.17.2)
* ```numpy``` (tested on 1.18.1)


#### Installation

Install by running the following commands
```
git clone https://github.com/ymzhang01/access-control.git
cd access-control
pip install -e .
```

#### Example
The example below generates an episode of length 1000 using a random policy

```
import gym

env = gym.make('access_control:AccessControl-v0')
state = env.reset()
for _ in range(1000):
    action = env.action_space.sample()
    next_state, reward, _, _ = env.step(action)
env.close() 
```



