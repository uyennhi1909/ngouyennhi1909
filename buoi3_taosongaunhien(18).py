# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:09:07 2024

@author: UNHI
"""

# Tạo số ngẫu nhiên theo yêu cầu pg.18

import random

# Một số ngẫu nhiên từ dãy (start,stop,step)

print("Số chẵn ngẫu nhiên từ 1 đến 10 là: ", random.randrange(2,10,2))
print("Số lẻ ngẫu nhiên từ 1 đến 10 là: ", random.randrange(1,10,2))

# Một số thực ngẫu nhiên r trong đoạn [x,y]

number = random.uniform(1,10)
print(f"Số thực ngẫu nhiên trong đoạn từ 1 đến 10 là: {number:.2f}")