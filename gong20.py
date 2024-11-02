#!/usr/bin/env python3

import time
import subprocess


def main():
    while True:
        countdown(1200)
        gong_for(5)


def gong_for(gong_secs):
    subprocess.run(['timeout', ('%ss' % gong_secs), 'paplay', 'gong.mp3'])


def countdown(timeout):
    while timeout > 0:
        mins, secs = divmod(timeout, 60)
        time_format = f"{mins:02}:{secs:02}"
        print(f"\r{time_format}", end="")
        time.sleep(1)
        timeout -= 1
    print("\r00:00")


if __name__ == "__main__":
    main()
