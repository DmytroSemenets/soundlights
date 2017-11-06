import sys
import socket
import array


COLORS_COUNT = 256
COLORS_OFFSET = 50


def get_spaced_colors(n):
    max_value = 16581375
    interval = int(max_value / n)
    colors = [hex(i)[2:].zfill(6) for i in range(0, max_value, interval)]

    return [(int(color[:2], 16),
             int(color[2:4], 16),
             int(color[4:6], 16)) for color in colors]


def send(colors):
    line = array.array('B', colors).tostring()
    sock.sendto(line, ('255.255.255.255', 42424))


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

colors = get_spaced_colors(COLORS_COUNT)

while True:
    try:
        nums = map(int, sys.stdin.readline()[:-1].split())
        led_colors = [c for num in nums for c in colors[num]]
        send(led_colors)
    except Exception as e:
        print(e)



