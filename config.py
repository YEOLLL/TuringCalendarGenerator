import toml
from PIL import ImageFont


def load_config(config_path):
    with open(config_path, 'r') as f:
        config = toml.loads(f.read())
    # 将 颜色 从 list 转换为 tuple
    # 将 字体文件路径和字体大小 转换为 ImageFont
    for key in config.keys():
        if 'color' in config[key]:
            config[key]['color'] = tuple(config[key]['color'])
        if 'weekday_color' in config[key]:
            config[key]['weekday_color'] = tuple(config[key]['weekday_color'])
        if 'weekend_color' in config[key]:
            config[key]['weekend_color'] = tuple(config[key]['weekend_color'])
        if 'font' in config[key]:
            config[key]['font'] = ImageFont.truetype('assets/'+config[key]['font'], config[key]['font_size'])
    config['table']['today']['font'] = ImageFont.truetype(
        'assets/'+config['table']['today']['font'],
        config['table']['today']['font_size'])
    config['table']['date']['font'] = ImageFont.truetype(
        'assets/'+config['table']['date']['font'],
        config['table']['date']['font_size'])
    config['table']['date_cn']['font'] = ImageFont.truetype(
        'assets/'+config['table']['date_cn']['font'],
        config['table']['date_cn']['font_size'])

    return config
