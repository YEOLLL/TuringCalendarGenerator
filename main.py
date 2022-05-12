import click
from PIL import Image
from calendar import generate
from wallpapaer import combine

from config import load_config


@click.group()
def cli():
    pass


@cli.command()
@click.option('-c', '--config', default='config.toml', help='配置文件路径')
@click.option('--transparent', is_flag=True)
def calendar(config, transparent):
    config = load_config(config_path=config)
    calendar_image = generate(config, transparent)
    calendar_image.save(config['calendar']['output'], 'png')
    click.echo(f"日历已保存至 {config['calendar']['output']}")


@cli.command()
@click.option('-c', '--config', default='config.toml', help='配置文件路径')
def wallpaper(config):
    config = load_config(config_path=config)
    calendar_image = generate(config, transparent=True)
    wallpaper_image = Image.open(config['wallpaper']['input'])
    wallpaper_image = combine(calendar_image, wallpaper_image,
                              config['wallpaper']['zoom'],
                              config['wallpaper']['pos'])
    wallpaper_image.save(config['wallpaper']['output'], 'png')
    click.echo(f"壁纸已保存至 {config['wallpaper']['output']}")


if __name__ == '__main__':
    cli()
