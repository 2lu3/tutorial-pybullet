import pybullet as p
import pybullet_data
from typing import List
import time

# -------------------------------------------
# 定数
# -------------------------------------------

# シミュレーションする時間(s)
total_time = 10
# シミュレーション幅(短いほど正確)
time_step = 0.01
# 3D画面の表示を表示するかどうか
visualize = True

# 初期座標
init_pos = [0, 0, 1]

# 重力
#gravity = [0, 0, -9.8]
gravity = [0, 0, 0]

# ファイル名
file_path = "robot.urdf"

# -------------------------------------------
# 初期化
# -------------------------------------------

# 3D画面の表示を切り変える
physicsClient: int
if visualize:
    # 3D画面表示
    physicsClient = p.connect(p.GUI)
else:
    # 3D画面非表示
    physicsClient = p.connect(p.DIRECT)

# time_step を設定
p.setTimeStep(time_step)

# 重力
p.setGravity(gravity[0], gravity[1], gravity[2])

# 地面の読み込み
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")

# URDFファイルの読み込み
robot_id = p.loadURDF(file_path, init_pos)

for i in range(int(total_time / time_step)):
    p.stepSimulation()
    time.sleep(time_step)

