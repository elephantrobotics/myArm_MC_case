import time

from pymycobot import MyArmM

mc = MyArmM("COM36", 1000000)

for i in range(8):
    mc.set_servo_enabled(i, 1)
    time.sleep(1)

# mc.set_joint_angle(7, -20, 20)
# mc.set_joints_angle([23.64, 13.02, 41.29, -1.05, 30.84, 27.24, -116], 30)


# print(mc.get_joints_angle())

# 先到零点
# 在到绿色方块上方 [23.64, 9.59, 27.58, -0.87, 64.33, 27.5, -116]
# 准备夹取绿色方块 [23.64, 13.02, 41.29, -1.05, 30.84, 27.24, -116]
# 夹取后回到绿色方块上方


