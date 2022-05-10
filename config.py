from PIL import ImageFont
from datetime import datetime

today = datetime.today()  # 日期，datetime 类型
title_text = ''  # 标题
description_text = ''''''  # 介绍语
code = ''''''  # 代码块
language = 'python'  # 代码块的语言，填 None 自动识别
filename = 'output.png'  # 输出文件名

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
