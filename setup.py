from setuptools import find_packages
from distutils.core import setup

setup(name='unitree_rl_gym_walkthrough',
      version='1.0.0',
      author='Tang, Feitong',
      license="BSD-3-Clause",
      packages=find_packages(),
      author_email='feitong_Tang@163.com',
      description='Walkthrough for Unitree Robots',
      install_requires=['isaacgym', 'rsl-rl', 'matplotlib', 'numpy==1.20', 'tensorboard', 'mujoco==3.2.3', 'pyyaml'])
