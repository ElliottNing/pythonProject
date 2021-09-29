# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    curr = time.time() * 1000
    print("当前时间：" , curr)
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("结束时间：", time.time()* 1000 - curr, "ms")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

