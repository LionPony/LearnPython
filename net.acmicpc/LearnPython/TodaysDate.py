# 오늘 날짜
# https://www.acmicpc.net/problem/10699
from datetime import datetime, timezone, timedelta

def solution():
    now_Utc = datetime.now(timezone.utc)
    now_Kst = now_Utc + timedelta(hours=9)
    print(now_Kst.strftime("%Y-%m-%d"))

solution()