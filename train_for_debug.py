import os
import subprocess

env = "a2d2_flux_controlnet_lora"

os.environ["CUDA_VISIBLE_DEVICES"] = "7"
os.environ["CONFIG_BACKEND"] = "json"
os.environ["ENV"] = env
os.environ["ENV_PATH"] = f"{env}/"
os.environ["CONFIG_PATH"] = f"config/{env}/config"
p = subprocess.run([
    "python", "train.py",
])
p.wait()