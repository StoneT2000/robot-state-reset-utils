import gymnasium as gym
from typing import TypeVar
MS2State = TypeVar("MS2State") # usually a flat vector
class ManiSkill2StateResetWrapper(gym.Wrapper):
    def set_env_state(self, state: MS2State):
        return self.env.unwrapped.set_state(state)
    def get_env_state(self) -> MS2State:
        return self.env.unwrapped.get_state()
    def get_env_obs(self):
        return self.env.unwrapped.get_obs()
