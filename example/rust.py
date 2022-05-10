from PIL import ImageFont
from datetime import datetime

today = datetime.today()
title_text = 'Rust'
description_text = '''Rust是由Mozilla主导开发的通用、编译型编程语言。设计准则为“安全、并发、实用”，
支持函数式、並行式、过程式以及面向对象的程式設計风格，专注于强大的编译时正确性
保证。它通过提供非常强大的编译时保证和对内存生命周期的明确控制，改进了其他系统
语言（如 C++，D 和 Cyclone）的思想。强大的内存保证使编写正确的并发代码比其他语
言更加容易。
'''
code = r'''
use chrono::prelude::*;

fn main() {
    let utc: DateTime<Utc> = Utc::now();
    println!("{}", utc.format("%Y-%m-%d").to_string());
}
'''
language = 'rust'
filename = 'rust.png'

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
description_pos = (150, 1750)  # 介绍语
calendar_table_pos = [(150, 2140), (1725, 2470)]  # 周历
code_pos = (250, 800)  # 代码块
