import pyautogui
import time
# nếu không có thư viện pyautogui thì chạy câu lệnh pip install pyautogui trong terminal

try:
    while True:
        # Lấy vị trí hiện tại của con trỏ chuột
        x, y = pyautogui.position()
        print(f"Tọa độ chuột: X = {x}, Y = {y}")
        time.sleep(0.5)  # Lấy tọa độ mỗi 0.5 giây
except KeyboardInterrupt:
    print("Đã dừng chương trình.")
