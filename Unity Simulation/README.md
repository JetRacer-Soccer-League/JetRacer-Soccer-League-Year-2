
## Introduction

The simulation environment will be used for training our rc car ai agents with reinforcement learning. Unity provides an [ml-agents library](https://github.com/Unity-Technologies/ml-agents) that can be used for training our agents. The [ml-agents library](https://github.com/Unity-Technologies/ml-agents) conveniently contains an example soccer twos simulation that we can adapt to our needs. Ideally, we would like to gather predictions on the throttle and steering angle that should be applied to our rc cars based on their camera feeds.

### Replicating physicality of RC cars

Current State:

The dimensions of the agent's game object has been modified to roughly rectangularly approximate the rc car. Instructions for doing this can be found in [SETUP.md](./SETUP.md).

Future Work:

The size and weight of the cars, friction of the wheels, etc. must also be replicated. This can be done by modifying the game objects of the agents in Unity.

### Action Space

The example simulation uses discrete values for its action space. This means that the agents in the example simulation can move left, right, forward, and backwards. In efforts to make the agents in the simulation behave like our rc cars, we must modify the action space to take continuous values of throttle and steering angle.

Current State:

The [AgentSoccer.cs script](./AgentSoccer.cs) has been modified to roughly replicate the rc car movement behavior. The expected output from the trained model should be continuous values between -1 and 1 for both the throttle and steering angle.

Future Work:

The vehicles movement in the simulation must be represented roughly one to one with our real life rc cars. This will involve modifying the movement behaviour of the agents in the simulation in the [AgentSoccer.cs script](./AgentSoccer.cs). 


### Observation Space

The observation space of the agents in the simulation are rays that come out of the agent's game object in equally spaced intervals. These rays detect the class of an object (ball, ally car, enemy car, ally goal, enemy goal, boundary) and its respective distance.

Current State:

The rays that come out of the back of the agent's game object have been removed because we cannot collect data about what is behind the rc cars.

Future Work:

A middleware must be developed to translate the object detection model's output to input for the simulation's observation space. This middleware should take the bounding boxes and class of the object from the object detection model, calculate the distance of the object, then assign the class and distance of the object to the respective observation ray.

### Known Issues

After the modifications in [SETUP.md](./SETUP.md) are made and the simulation is training, the frame rate is extremely low. The ball and agents are observed to be moving, but sometimes the ball moves without any visible interaction with the agents.

# Unity ML-Agents Trainers

The `mlagents` Python package is part of the
[ML-Agents Toolkit](https://github.com/Unity-Technologies/ml-agents). `mlagents`
provides a set of reinforcement and imitation learning algorithms designed to be
used with Unity environments. The algorithms interface with the Python API
provided by the `mlagents_envs` package. See [here](../docs/Python-LLAPI.md) for
more information on `mlagents_envs`.

The algorithms can be accessed using the: `mlagents-learn` access point. See
[here](../docs/Training-ML-Agents.md) for more information on using this
package.

## Installation

Install the `mlagents` package with:

```sh
python -m pip install mlagents==1.0.0
```

## Usage & More Information

For more information on the ML-Agents Toolkit and how to instrument a Unity
scene with the ML-Agents SDK, check out the main
[ML-Agents Toolkit documentation](../docs/Readme.md).

## Limitations

- Resuming self-play from a checkpoint resets the reported ELO to the default
  value.
