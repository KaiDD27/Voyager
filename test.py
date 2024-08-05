from voyager import Voyager
import os


voyager = Voyager(
    #azure_login=azure_login,
    mc_port=65535,
    env_wait_ticks=100,
    env_request_timeout=1000,
    # 获取环境变量的值
    openai_api_key = os.getenv("OPENAI_API_KEY"),
    openai_api_request_timeout=500,
    #skill_library_dir="./skill_library/trial1", # Load a learned skill library.
    #ckpt_dir="./ckpt2", # Feel free to use a new dir. Do not use the same dir as skill library because new events will still be recorded to ckpt_dir. 
    #resume=False, # Do not resume from a skill library because this is not learning.
    resume=True,

)
# 运行任务分解
#task = "Craft a diamond pickaxe" # 例如 "制作一把钻石镐"
#sub_goals = voyager.decompose_task(task=task)
#voyager.inference(sub_goals=sub_goals)

voyager.learn()
#voyager.learn(reset_env=False)

