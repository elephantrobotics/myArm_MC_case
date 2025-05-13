# myarm_c.py - 读取myArmC角度并发送
import socket
from pymycobot import MyArmC
import serial.tools.list_ports
import time


def get_port():
    port_list = serial.tools.list_ports.comports()
    i = 1
    res = {}
    for port in port_list:
        print("{} - {}".format(i, port.device))
        res[str(i)] = port.device
        i += 1
    return res


def wait_for_button_press(c):
    print("等待按下红色按钮以启动摇操功能...")
    last_status = [0]
    while True:
        current_status = c.is_tool_btn_clicked(2)
        print(current_status)
        if current_status == [1] and last_status == [0]:
            print("检测到红色按钮按下，开始发送角度数据...")
            break
        last_status = current_status
        time.sleep(0.05)


def main():
    port_dict = get_port()
    port_c = input("input myArm C port: ")
    c_port = port_dict[port_c]
    c = MyArmC(c_port, debug=False)

    wait_for_button_press(c)

    # 建立 socket 连接
    HOST = '127.0.0.1'
    PORT = 8001
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        angle = c.get_joints_angle()
        if angle is not None:
            data = '\n' + str(angle)
            client.send(data.encode('utf-8'))
        time.sleep(0.05)  # 稍作延迟避免占用过高CPU


if __name__ == "__main__":
    main()
