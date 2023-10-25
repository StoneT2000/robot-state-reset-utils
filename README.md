# Robot Environment State Reset Utilities

A set of utilities and scripts to format demonstrations from various robotics benchmarks (MetaWorld, ManiSkill etc.) to support and leverage environment state reset. Demonstrations here are stored following the [ManiSkill2 demonstration format](https://haosulab.github.io/ManiSkill2/concepts/demonstrations.html#format), which flexibly supports environment states.

Why environment state reset? A number of recent approaches have demonstrated greater sample/demonstration efficiency (e.g. [Reverse Forward Curriculum Learning](https://stoneztao.com/rfcl)) and impressive results (e.g. [Sequential Dexterity](https://sequential-dexterity.github.io/))

Supported Benchmarks:
- [ManiSkill2](https://github.com/haosulab/ManiSkill2)
- [MetaWorld (using original MetaWorld version)](https://github.com/Farama-Foundation/Metaworld)
- [Adroit (originally from D4RL, now using Gymnasium-Robotics version)](https://github.com/Farama-Foundation/Gymnasium-Robotics)

Planned:
- Isaac Sim Environments

## Getting Started

Only a few dependencies install them as so

```bash
pip install gymnasium h5py
pip install mani-skill2
```


## Demonstration Formatting/Conversion

In `scripts/` there is a script for each benchmark and instructions for how to download/generate demonstrations.

To download already formatted demonstrations see the [hugging face dataset](https://huggingface.co/datasets/stonet2000/robot_demos_with_state_reset) or click the following to download directly: https://huggingface.co/datasets/stonet2000/robot_demos_with_state_reset/blob/main/demos.zip

## Environment State Reset Wrappers

To allow environment state reset, we recommend using the single-file wrappers provided in this repository (just copy the code, no need for a pip install) which work out of the box with the supported environments/benchmarks. They augment the existing environment with state reset functionality, in addition to fixing various weird bugs such as [this one](https://github.com/Farama-Foundation/Gymnasium-Robotics/issues/165) when it comes to state reset.

All state reset wrappers implement 3 methods

- `get_env_state(self) -> T` returns the current environmnet state. Depending on the environment this could be a flat vector or a dictionary.
- `set_env_state(self, state: T)` sets the environment using a state object. Anything returned by `get_env_state` can be used here.
- `get_env_obs(self)` returns the current environment observation. Useful for retrieving the current agent's observation once a state has been set. Note some benchmarks do not support this easily.