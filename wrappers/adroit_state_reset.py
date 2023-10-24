import gymnasium as gym
import numpy as np
from gymnasium_robotics.envs.adroit_hand.adroit_door import AdroitHandDoorEnv
from gymnasium_robotics.envs.adroit_hand.adroit_relocate import AdroitHandRelocateEnv
from typing import TypeVar
AdroitState = TypeVar("AdroitState") # usually a dictionary of vectors

class AdroitResetStateWrapper(gym.Wrapper):
    def set_env_state(self, state: AdroitState):
        env: AdroitHandDoorEnv = self.env.unwrapped
        if isinstance(env, AdroitHandRelocateEnv):
            # fix bug where Mujoco env cannot set state correctly in Relocate when there is close contact with ball
            # very strange error but I believe it may be due to the lower fidelity simulation Adroit envs use by default
            # See https://github.com/Farama-Foundation/Gymnasium-Robotics/issues/165
            qp = state["qpos"]
            qv = state["qvel"]
            env.model.body_pos[env.obj_body_id] = state["obj_pos"]
            env.model.site_pos[env.target_obj_site_id] = state["target_pos"]
            env.set_state(qp, qv)  # call this and let Mujoco step forward once
            diff = env.model.body_pos[env.obj_body_id] - env.data.xpos[env.obj_body_id]
            env.model.body_pos[env.obj_body_id] = state["obj_pos"] + diff
            return env.set_state(qp, qv)
        
        return env.set_env_state(state)
    def get_env_state(self) -> AdroitState:
        return self.env.unwrapped.get_env_state()
    def get_env_obs(self):
        return self.env.unwrapped._get_obs()