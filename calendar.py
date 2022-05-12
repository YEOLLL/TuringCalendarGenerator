from PIL import Image, ImageDraw
from datetime import timedelta, datetime
from lunar_python import Lunar

from code import highlight_image


# 水平方向由正方形构成的虚线
def draw_grid_line_h(draw, pos_x_list, pos_y, pixel_size, fill, gap):
    (x_begin, x_end) = pos_x_list
    for x in range(x_begin, x_end, pixel_size + gap):
        draw.rectangle(xy=(x, pos_y, x + pixel_size - 1, pos_y + pixel_size - 1), fill=fill)


# 绘制垂直方向由正方形构成的虚线
def draw_grid_line_v(draw, pos_y_list, pos_x, pixel_size, fill, gap):
    (y_begin, y_end) = pos_y_list
    for y in range(y_begin, y_end, pixel_size + gap):
        draw.rectangle(xy=(pos_x, y, pos_x + pixel_size - 1, y + pixel_size - 1), fill=fill)


# 绘制单格日历
def draw_calendar(draw, pos_list, config,
                  _today_text, _date_text, _date_cn_text):
    # 绘制边框
    draw_grid_line_h(
        draw, (pos_list[0][0], pos_list[1][0]), pos_list[0][1],
        config['table']['border'], config['table']['color'], config['table']['gap'])
    draw_grid_line_h(
        draw, (pos_list[0][0], pos_list[1][0]), pos_list[1][1],
        config['table']['border'], config['table']['color'], config['table']['gap'])
    draw_grid_line_v(
        draw, (pos_list[0][1], pos_list[1][1]), pos_list[0][0],
        config['table']['border'], config['table']['color'], config['table']['gap'])
    draw_grid_line_v(
        draw, (pos_list[0][1], pos_list[1][1]), pos_list[1][0],
        config['table']['border'], config['table']['color'], config['table']['gap'])
    # 补右下角像素点
    draw.rectangle(
        xy=(pos_list[1][0], pos_list[1][1],
            pos_list[1][0] + config['table']['border'] - 1, pos_list[1][1] + config['table']['border'] - 1),
        fill=config['table']['color'])

    # 假日显示特殊颜色
    if _today_text in ['Sat', 'Sun']:
        _today_color = _date_color = _date_cn_color = config['table']['weekend_color']
    else:
        _today_color = _date_color = _date_cn_color = config['table']['weekday_color']

    # 计算坐标信息
    [(x_begin, y_begin), (x_end, y_end)] = pos_list
    today_pos_x = date_pos_x = date_cn_pos_x = (x_begin + x_end) // 2
    temp = ((y_end - y_begin) // 4)
    today_pos_y = temp + y_begin
    date_pos_y = temp + today_pos_y
    date_cn_pos_y = temp + date_pos_y

    # 绘制信息
    draw.text(
        xy=(today_pos_x, today_pos_y), text=_today_text,
        fill=_today_color, font=config['table']['today']['font'], anchor='mm')
    draw.text(
        xy=(date_pos_x, date_pos_y), text=_date_text,
        fill=_date_color, font=config['table']['date']['font'], anchor='mm')
    draw.text(
        xy=(date_cn_pos_x, date_cn_pos_y), text=_date_cn_text,
        fill=_date_cn_color, font=config['table']['date_cn']['font'], anchor='mm')


# 绘制周历
def draw_calendar_table(draw, today, config):
    # 计算坐标
    ([x_begin, y_begin], [x_end, y_end]) = config['table']['pos']
    width = (x_end - x_begin) // 7

    # 绘制每一格日历
    weekday = today - timedelta(days=today.weekday())
    for _ in range(7):
        day = weekday.strftime('%a')  # 星期缩写
        date = weekday.strftime('%m-%d')  # 月-日
        # 中文日期，可以是节气、节日等
        lunar_weekday = Lunar.fromDate(weekday)
        festivals = lunar_weekday.getFestivals()
        date_cn_text = festivals[0][:-1] if len(festivals) != 0 else lunar_weekday.getDayInChinese()

        draw_calendar(draw, [(x_begin, y_begin), (x_begin + width, y_end)], config,
                      day, date, date_cn_text)

        weekday += timedelta(days=1)
        x_begin += width


# 生成图片
def generate(config, transparent=False):
    # 生成背景为 透明 / 白色 的图片
    calendar_size = (1888, 2572)
    if transparent:
        calendar_image = Image.new('RGBA', calendar_size, (255, 255, 255, 0))
    else:
        calendar_image = Image.new('RGBA', calendar_size, (255, 255, 255, 255))
    draw = ImageDraw.Draw(calendar_image)

    # 读取日期
    if config['calendar']['today'] == 'today':
        today = datetime.today()
    else:
        today = datetime.fromisoformat(config['calendar']['today'])

    # 格式化信息
    # 右上角日期
    date_text = today.strftime("%Y-%m-%d")
    # 右上角星期缩写
    today_text = today.strftime("%a")
    if today_text in ['Sat', 'Sun']:
        today_color = config['today']['weekend_color']
    else:
        today_color = config['today']['weekday_color']
    # 右上角中文日期，如果有节假日显示节假日名字，并使用 weekend_color
    lunar_today = Lunar.fromDate(today)
    festivals = lunar_today.getFestivals()
    if len(festivals) != 0:
        date_cn_text = festivals[0][:-1]
        date_cn_color = config['date_cn']['weekend_color']
    else:
        date_cn_text = lunar_today.getDayInChinese()
        date_cn_color = config['date_cn']['weekday_color']

    # 绘制
    # 标题
    draw.text(xy=config['title']['pos'],
              text=config['calendar']['title'],
              fill=config['title']['color'],
              font=config['title']['font'])
    # 日期
    draw.text(xy=config['date']['pos'],
              text=date_text,
              fill=config['date']['color'],
              font=config['date']['font'])
    # 星期
    draw.text(xy=config['today']['pos'],
              text=today_text,
              fill=today_color,
              font=config['today']['font'])
    # 中文日期
    draw.text(xy=config['date_cn']['pos'],
              text=date_cn_text,
              fill=date_cn_color,
              font=config['date_cn']['font'])

    # 代码图
    code_image = highlight_image(config['calendar']['code'],
                                 config['code']['font_size'],
                                 config['code']['line_pad'],
                                 config['calendar']['language'])
    temp_image = Image.new('RGBA', calendar_size, (255, 255, 255, 0))
    temp_image.paste(code_image, config['code']['pos'])
    calendar_image.alpha_composite(temp_image)

    # 介绍语
    draw.multiline_text(xy=config['description']['pos'],
                        text=config['calendar']['description'],
                        fill=config['description']['color'],
                        font=config['description']['font'],
                        spacing=config['description']['spacing'])
    draw_calendar_table(draw, today, config)  # 最下方周历表

    # calendar_image.show()
    return calendar_image
