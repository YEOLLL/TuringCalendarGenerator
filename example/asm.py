from PIL import ImageFont
from datetime import datetime

today = datetime.today()
title_text = 'Assembly Language'
description_text = '''汇编语言（assembly language）是一种用于电子计算机、微处理器、微控制器，或其他可
编程器件的低级语言，最早于 1949 年出现，在不同的设备中，汇编语言对应着不同的机器
言指令集。一种汇编语言专用于某种计算机系统结构，而不像许多高级语言可以在不同的系
统平台自己移植
'''
code = r'''
call get_date \ lea dx, date
mov ah, 09h \ int 21h \ mov ax, 4c00h
int 21h
date:
db "0000-00-00", 0ah, 0dh, '$'
get_date:
mov al, 04h \ int 1ah \ mov bx, offset date
mov al, dl \ call put_bcd2 \ inc bx
mov al, dh \ call put_bcd2 \ inc bx
mov al, ch \ call put_bcd2 \ mov al, cl
call put_bcd2 \ ret
put_bcd2:
push ax \ shr ax, 4 ] and ax, 0fh
add ax, '0' \ mov [bx], al \ inc bx
pop ax, \ and ax, 0fh \ add ax, '0'
mov [bx], al \ inc bx \ ret
'''
language = 'nasm'
filename = 'asm.png'

# 字体
title_font = ImageFont.truetype('assets/SpaceMono-Bold.ttf', 120)  # 标题
date_font = ImageFont.truetype('assets/SpaceMono-Regular.ttf', 80)  # 日期
today_font = ImageFont.truetype('assets/SpaceMono-Regular.ttf', 60)  # 今日
date_cn_font = ImageFont.truetype('assets/NotoSansSC-Regular.otf', 50)  # 汉语日期
description_font = ImageFont.truetype('assets/NotoSansSC-Regular.otf', 40)  # 介绍语
calendar_table_today_font = ImageFont.truetype('assets/SpaceMono-Bold.ttf', 70)  # 周历今日
calendar_table_date_font = ImageFont.truetype('assets/SpaceMono-Regular.ttf', 35)  # 周历日期
calendar_table_date_cn_font = ImageFont.truetype('assets/NotoSansSC-Regular.otf', 40)  # 周历汉语日期
code_font_size = 40

# 颜色
title_color = (35, 31, 32)  # 标题
date_color = (35, 31, 32)  # 日期
weekday_color = (35, 31, 32)  # 工作日
weekend_color = (218, 40, 34)  # 周末
description_color = (107, 105, 106)  # 介绍语
calendar_table_color = (107, 106, 106)  # 周历边框

# 位置
title_pos = (150, 300)  # 标题
date_pos = (1250, 500)  # 日期
today_pos = (1500, 625)  # 今日
date_cn_pos = (1640, 635)  # 汉语日期
description_pos = (150, 1800)  # 介绍语
calendar_table_pos = [(150, 2140), (1725, 2470)]  # 周历
code_pos = (250, 750)  # 代码块
