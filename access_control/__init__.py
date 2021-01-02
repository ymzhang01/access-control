from gym.envs.registration import register

register(
    id='AccessControl-v0',
    entry_point='access_control.envs:AccessControlEnv',
)