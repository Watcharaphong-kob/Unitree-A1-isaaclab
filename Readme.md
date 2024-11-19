# Project Setup

This guide will help you set up your environment to use NVIDIA Isaac Sim and clone the NVIDIA Isaac Lab repository.

## Prerequisites

- Ensure you have Python 3.6 or later installed.
- Ensure you have Git installed.

## Installation

### Step 1: Install NVIDIA Isaac Sim

1. Download the NVIDIA Isaac Sim package from the [NVIDIA Developer website](https://developer.nvidia.com/isaac-sim).
2. Follow the installation instructions provided on the website.

### Step 2: Clone the NVIDIA Isaac Lab Repository

1. Open a terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command to clone the repository:

    ```sh
    git clone https://github.com/isaac-sim/IsaacLab.git
    ```

4. Navigate into the cloned repository:

    ```sh
    cd IsaacLab
    ```
## Workspace Customization for Unitree A1

Edit or add 
1. Navigate to Wrapper Folder commonly in
```
\source\extensions\omni.isaac.lab_tasks\omni\isaac\lab_tasks\manager_based\locomotion\velocity\config\a1
```
2. After Add new Wrapper in config you need to initialize the Wrapper in 
```
\manager_based\locomotion\velocity\__init__.py
```
3. You can also adding new rewarding in the 
```
\manager_based\locomotion\velocity\velocity_env_cfg.py
```
## Additional Resources

- [NVIDIA Isaac Sim Documentation](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/overview.html)
- [NVIDIA Isaac Lab Documentation](https://isaac-sim.github.io/IsaacLab/main/)
- [NVIDIA Isaac Lab Documentation](https://github.com/isaac-sim/IsaacLab)

