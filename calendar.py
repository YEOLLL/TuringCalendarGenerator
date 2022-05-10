from PIL import Image, ImageDraw
from datetime import datetime, timedelta
from lunar_python import Lunar

from code import highlight_image
from config import *


# 水平方向由正方形构成的虚线
def draw_grid_line_h(_draw, pos_x_list, pos_y, pixel_size, fill, gap):
    (x_begin, x_end) = pos_x_list
    for x in range(x_begin, x_end, pixel_size + gap):
        _draw.rectangle(xy=(x, pos_y, x + pixel_size - 1, pos_y + pixel_size - 1), fill=fill)


# 绘制垂直方向由正方形构成的虚线
def draw_grid_line_v(_draw, pos_y_list, pos_x, pixel_size, fill, gap):
    (y_begin, y_end) = pos_y_list
    for y in range(y_begin, y_end, pixel_size + gap):
        _draw.rectangle(xy=(pos_x, y, pos_x + pixel_size - 1, y + pixel_size - 1), fill=fill)


# 绘制单格日历
def draw_calendar(_draw, pos_list, border_width, border_color, gap,
                  _today_text, _date_text, _date_cn_text):
    # 绘制边框
    draw_grid_line_h(
        _draw, (pos_list[0][0], pos_list[1][0]), pos_list[0][1], border_width, border_color, gap)
    draw_grid_line_h(
        _draw, (pos_list[0][0], pos_list[1][0]), pos_list[1][1], border_width, border_color, gap)
    draw_grid_line_v(
        _draw, (pos_list[0][1], pos_list[1][1]), pos_list[0][0], border_width, border_color, gap)
    draw_grid_line_v(
        _draw, (pos_list[0][1], pos_list[1][1]), pos_list[1][0], border_width, border_color, gap)
    # 补右下角像素点
    _draw.rectangle(
        xy=(pos_list[1][0], pos_list[1][1], pos_list[1][0] + border_width - 1, pos_list[1][1] + border_width - 1),
        fill=border_color)

    # 假日显示特殊颜色
    _today_color = _date_color = weekend_color if _today_text in ['Sat', 'Sun'] else weekday_color
    _date_cn_color = _today_color
    # 计算坐标信息
    [(x_begin, y_begin), (x_end, y_end)] = pos_list
    today_pos_x = date_pos_x = date_cn_pos_x = (x_begin + x_end) // 2
    temp = ((y_end - y_begin) // 4)
    today_pos_y = temp + y_begin
    date_pos_y = temp + today_pos_y
    date_cn_pos_y = temp + date_pos_y

    # 绘制信息
    _draw.text(
        xy=(today_pos_x, today_pos_y), text=_today_text,
        fill=_today_color, font=calendar_table_today_font, anchor='mm')
    _draw.text(
        xy=(date_pos_x, date_pos_y), text=_date_text,
        fill=_date_color, font=calendar_table_date_font, anchor='mm')
    _draw.text(
        xy=(date_cn_pos_x, date_cn_pos_y), text=_date_cn_text,
        fill=_date_cn_color, font=calendar_table_date_cn_font, anchor='mm')


# 绘制周历
def draw_calendar_table(_draw, today, pos_list):
    # 计算坐标
    [(x_begin, y_begin), (x_end, y_end)] = pos_list
    width = (pos_list[1][0] - pos_list[0][0]) // 7

    # 绘制每一格日历
    weekday = today - timedelta(days=today.weekday())
    for _ in range(7):
        day = weekday.strftime('%a')  # 星期缩写
        date = weekday.strftime('%m-%d')  # 月-日
        # 中文日期，可以是节气、节日等
        lunar_weekday = Lunar.fromDate(weekday)
        festivals = lunar_weekday.getFestivals()
        date_cn_text = festivals[0][:-1] if len(festivals) != 0 else lunar_weekday.getDayInChinese()

        draw_calendar(_draw, [(x_begin, y_begin), (x_begin + width, y_end)], 5, calendar_table_color, 5,
                      day, date, date_cn_text)

        weekday += timedelta(days=1)
        x_begin += width


# 生成图片
def generate(_today, _title_text, _description_text, _code, _language, _filename='output.png'):
    # 生成背景为 透明 / 白色 的图片
    calendar_size = (1888, 2572)
    calendar_image = Image.new('RGBA', calendar_size, (255, 255, 255))
    # img = Image.new('RGB', (1888, 2572), (255, 255, 255))
    draw = ImageDraw.Draw(calendar_image)

    date_text = _today.strftime("%Y-%m-%d")  # 右上角日期
    today_text = _today.strftime("%a")  # 右上角星期缩写
    # 右上角中文日期，如果有节假日显示节假日名字，并使用 weekend_color
    lunar_today = Lunar.fromDate(_today)
    festivals = lunar_today.getFestivals()
    if len(festivals) != 0:
        date_cn_text = festivals[0][:-1]
        date_cn_color = weekend_color
    else:
        date_cn_text = lunar_today.getDayInChinese()
        date_cn_color = weekday_color

    # 绘制
    draw.text(xy=title_pos, text=_title_text, fill=title_color, font=title_font)  # 标题
    draw.text(xy=date_pos, text=date_text, fill=date_color, font=date_font)  # 日期
    today_color = weekend_color if today_text in ['Sat', 'Sun'] else weekday_color
    draw.text(xy=today_pos, text=today_text, fill=today_color, font=today_font)  # 星期
    draw.text(xy=date_cn_pos, text=date_cn_text, fill=date_cn_color, font=date_cn_font)  # 中文日期

    code_image = highlight_image(_code, _language)
    temp_image = Image.new('RGBA', calendar_size, (255, 255, 255, 0))
    temp_image.paste(code_image, code_pos)
    calendar_image.alpha_composite(temp_image)

    draw.multiline_text(xy=description_pos,
                        text=_description_text,
                        fill=description_color,
                        font=description_font,
                        spacing=20)  # 介绍语
    draw_calendar_table(draw, _today, calendar_table_pos)  # 最下方周历表

    # calendar_image.show()
    calendar_image.save(_filename, 'png')
