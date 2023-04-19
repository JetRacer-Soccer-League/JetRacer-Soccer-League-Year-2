# Setup

The following steps were followed to set up the Unity ml-agents simulation environment.
These steps were found in the ml-agents repostitory installation guide here: https://github.com/Unity-Technologies/ml-agents/blob/develop/docs/Installation.md

1. Install Unity Game Engine
2. Install Python (Must be compatible with ml-agents package) (3.9.16 was compatible with ml-agents as of 4/19/2023)
3. Clone the ml-agents repository (https://github.com/Unity-Technologies/ml-agents)
    ```
    git clone --branch release_19 https://github.com/Unity-Technologies/ml-agents.git
    ```
4. In Unity Hub, click Open -> Add Project From Disk, navigate to the cloned ml-agents repository and select the Project folder, then add project
5. Create a virtual environment with pip and activate it.
6. Install torch, ml-agents-envs, and ml-agents to the virtual environment. IMPORTANT! Install these packages in this order as the `mlagents` package depends on `mlagents_envs`. First navigate to the cloned ml-agents repostitory.
    ```
    pip install torch -f https://download.pytorch.org/whl/torch_stable.html
    pip install -e ./ml-agents-envs
    pip install -e ./ml-agents
    ```
7. The soccer environment example can be loaded in to Unity by navigating to Assets/ML-Agents/Examples/Soccer/Scenes in the project area of Unity then dragging the `SoccerTwos` scene into the Project Hierarchy.
