import pybullet as p
import pybullet_data
import time
import matplotlib.pyplot as plt

# -------------------------------------------
# 定数
# -------------------------------------------

# シミュレーションする時間(s)
total_time = 5
# シミュレーション幅(短いほど正確)
time_step = 0.01
# 再生速度
replay_speed = 1

# 3D画面の表示を表示するかどうか
visualize = True

# 初期座標
init_pos = [0, 0, 1]


# 重力
gravity = [0, 0, -9.8]
#gravity = [0, 0, 0]

# ファイル名
file_path = "ball.urdf"

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
base_id = p.loadURDF("base.urdf")
p.changeDynamics(base_id, -1, restitution=0.9, lateralFriction=0.9)

# URDFファイルの読み込み
robot_id = p.loadURDF(file_path, init_pos, flags= p.URDF_USE_INERTIA_FROM_FILE)
p.changeDynamics(robot_id, -1, restitution=0.9, lateralFriction=0.9)

# -------------------------------------------
# シミュレーション
# -------------------------------------------

log_z = []
for i in range(int(total_time / time_step)):
    p.stepSimulation()
    position, orientation = p.getBasePositionAndOrientation(robot_id)
    log_z.append(position[2])
    if visualize:
        time.sleep(time_step / replay_speed)


# -------------------------------------------
# 可視化
# -------------------------------------------

plt.figure()
plt.plot(log_z)
plt.show()
