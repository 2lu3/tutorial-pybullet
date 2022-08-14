import pybullet as p
import pybullet_data
import time
import matplotlib.pyplot as plt

# -------------------------------------------
# 定数
# -------------------------------------------

# シミュレーションする時間(s)
total_time = 3
# シミュレーション幅(短いほど正確)
time_step = 0.01
# 再生速度
replay_speed = 1

# 3D画面の表示を表示するかどうか
visualize = True


# 重力
gravity = [0, 0, -9.8]
#gravity = [0, 0, 0]

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

# -------------------------------------------
# URDFの読み込み
# -------------------------------------------

# 地面の読み込み
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")

# ボール
ball_id = p.loadURDF("ball.urdf", [0, 1, 0])
p.changeDynamics(ball_id, -1, restitution=0.9, lateralFriction=0.9)

# ローラー
roller_id = p.loadURDF("roller.urdf", [0, 0, 0.5])
p.changeDynamics(roller_id, -1,mass=0, restitution=0.9, lateralFriction=0.9)

# -------------------------------------------
# シミュレーション
# -------------------------------------------

# 初期速度の設定
p.resetBaseVelocity(ball_id, [0, -1, 0])

log = []
for i in range(int(total_time / time_step)):

    # ローラーの速度設定
    p.setJointMotorControl2(roller_id, 0, controlMode=p.VELOCITY_CONTROL, targetVelocity=10, force=500)
    p.setJointMotorControl2(roller_id, 1, controlMode=p.VELOCITY_CONTROL, targetVelocity=-10, force=500)

    p.stepSimulation()

    position, orientation = p.getBasePositionAndOrientation(ball_id)
    log.append(position[1])

    if visualize:
        time.sleep(time_step / replay_speed)


# -------------------------------------------
# 可視化
# -------------------------------------------

plt.figure()
plt.plot(log)
plt.show()
