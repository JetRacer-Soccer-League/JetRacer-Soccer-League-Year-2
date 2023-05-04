# Setup

The following steps were followed to set up the Unity ml-agents simulation environment.
These steps were found in the ml-agents repostitory installation guide here: https://github.com/Unity-Technologies/ml-agents/blob/develop/docs/Installation.md

1. Install Unity Game Engine
2. Install Python 3.8.6 (Must be compatible with ml-agents package). IMPORTANT: Must use this version of python for the environment
3. Clone the ml-agents repository (https://github.com/Unity-Technologies/ml-agents)
    ```
    git clone --branch release_19 https://github.com/Unity-Technologies/ml-agents.git
    ```
4. Create a virtual environment in ml-agents package. Activate it
    ```
    cd ml-agents
    pip install virtualenv
    virtualenv -p [path to python.exe of the correct version] soccerenv
    source soccerenv/Scripts/activate
    ```
6. Install torch, ml-agents-envs, and ml-agents to the virtual environment. IMPORTANT! Install these packages in this order as the `mlagents` package depends on `mlagents_envs`. First navigate to the cloned ml-agents repostitory.
    ```
    pip install torch -f https://download.pytorch.org/whl/torch_stable.html
    pip install -e ./ml-agents-envs
    pip install -e ./ml-agents
    ```
7. Downgrade numpy version to 1.19 in order for it to be compatible with mlagents package.
    ```
    pip install numpy==1.19
    ```
8. In Unity Hub, click Open -> Add Project From Disk, navigate to the cloned ml-agents repository and select the Project folder, then add project

9. The soccer environment example can be loaded in to Unity by navigating to Assets/ML-Agents/Examples/Soccer/Scenes in the project area of Unity then dragging the `SoccerTwos` scene into the Project Hierarchy.
10. Replace the AgentSoccer.cs script with the AgentSoccer.cs script in the JetRacer-Soccer-Leage-Year-2 repository.
11. Click on the 'SoccerFieldTwos' object in the project hierarchy in Unity. In the inspector, click on open next to prefab. For each soccer agent:
    - Click on the AgentCube child object. Change the Scale to X=1.5, Y=1, Z=3.
    - Click on the backwards sensors child object. Delete it.
    - Under behavior parameters, change the vector observation space size to 2, continuous actions to  2, discrete branches size to 0.
12. Navigate to the ml-agents package and begin training.
    ```
    cd ml-agents
    mlagents-lean config/poca/SoccerTwos.yaml --run-id=[whatever name you would like]
    ```
    When prompted to, click play in the Unity game engine. The agents should start training.