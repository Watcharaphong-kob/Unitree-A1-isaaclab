# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from omni.isaac.lab.utils import configclass
from .rough_env_cfg import UnitreeA1RoughEnvCfg
from omni.isaac.lab.envs import ManagerBasedRLEnv
from ...velocity_env_cfg import CommandsCfg

@configclass
class UnitreeA1StandEnvCfg(UnitreeA1RoughEnvCfg):
    def __post_init__(self):
        # Post-init of parent configuration
        super().__post_init__()

        self.scene.robot.init_state.pos =(0.0, 0.0, 0.15)  # Set initial position
        crouch_position = [0.1, 1.2, -2.3]  # Example crouched joint angles
        self.scene.robot.init_state.joint_pos = {
            ".*L_hip_joint": crouch_position[0],  # Neutral hip position
            ".*R_hip_joint": crouch_position[0],  # Neutral hip position
            "F[L,R]_thigh_joint": crouch_position[1],  # More bent forward legs
            "R[L,R]_thigh_joint": crouch_position[1],  # More bent backward legs
            ".*_calf_joint": crouch_position[2],  # Neutral calf position
        } 
        
        # Override rewards to emphasize standing behavior and penalize movement
        self.rewards.feet_air_time.weight = -0.5 # No reward for feet air time
        self.rewards.flat_orientation_l2.weight = -3  # Penalize orientation deviation
        # self.rewards.lin_vel_z_l2.weight = 2
        self.rewards.track_lin_vel_xy_exp.weight = -0.1  # Penalize linear movement
        self.rewards.track_ang_vel_z_exp.weight = -0.1  # Penalize angular movement
        self.rewards.ang_vel_xy_l2.weight = -0.1 # Penalize angular movement
        
        self.rewards.target_height_reward.weight = 3  # Reward standing height
      
        # Change terrain to flat
        self.scene.terrain.terrain_type = "plane"
        self.scene.terrain.terrain_generator = None
        
        # No height scan
        self.scene.height_scanner = None
        self.observations.policy.height_scan = None
        
        # No terrain curriculum
        self.curriculum.terrain_levels = None
        
        # self.events.reset_robot_joints.params["position_range"] = (-2.8, 2.8)
        
@configclass
class UnitreeA1StandEnvCfg_PLAY(UnitreeA1StandEnvCfg):
    def __post_init__(self) -> None:
        # Post-init of parent configuration
        super().__post_init__()

        # Make a smaller scene for play
        self.scene.num_envs = 50
        self.scene.env_spacing = 2.5
        
        # Disable randomization for play
        self.observations.policy.enable_corruption = False
        
        # Remove random pushing event
        self.events.base_external_force_torque = None
        self.events.push_robot = None
