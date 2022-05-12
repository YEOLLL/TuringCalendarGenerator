from PIL import Image
from io import BytesIO
from pygments import highlight
from pygments.lexers import guess_lexer, get_lexer_by_name
from pygments.formatters import ImageFormatter
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, \
    Number, Operator, Punctuation, Token, Text


# 修改自 style/onedark.py
class OneDarkStyle(Style):
    default_style = ''
    background_color = '#00000000'  # 背景透明
    # background_color = '#ffffff'
    styles = {
        Token:                  '#ABB2BF',

        Punctuation:            '#ABB2BF',
        Punctuation.Marker:     '#ABB2BF',

        Keyword:                '#C678DD',
        Keyword.Constant:       '#E5C07B',
        Keyword.Declaration:    '#C678DD',
        Keyword.Namespace:      '#C678DD',
        Keyword.Reserved:       '#C678DD',
        Keyword.Type:           '#E5C07B',

        Name:                   '#E06C75',
        Name.Attribute:         '#E06C75',
        Name.Builtin:           '#E5C07B',
        Name.Class:             '#E5C07B',
        Name.Function: '#61AFEF',  # 去除粗体
        Name.Function.Magic: '#56B6C2',  # 去除粗体
        Name.Other: '#E06C75',
        Name.Tag: '#E06C75',
        Name.Decorator: '#61AFEF',
        Name.Variable.Class: '',

        String: '#98C379',

        Number: '#D19A66',

        Operator: '#56B6C2',

        Comment: '#7F848E'
    }


class OneHalfLightStyle(Style):
    default_style = ''
    background_color = '#00000000'
    styles = {
        Comment: '#A0A1A7',

        Text: "#383A42",

        Keyword: '#A626A4',
        Keyword.Constant: '#C18401',

        Name.Variable: '#E45649',
        Name.Function: '#0184BC',
        Name.Class: '#C18401',

        String: '#50A14F',

        Number.Integer: '#C18401',
        Number.Float: '#C18401',
    }


def highlight_image(code, font_size, line_pad, language):
    if language is not None:
        lexer = get_lexer_by_name(language)
    else:
        lexer = guess_lexer(code)

    formatter = ImageFormatter(line_numbers=False, image_format='png',
                               font_size=font_size, line_pad=line_pad, style=OneHalfLightStyle)
    image_bytes = BytesIO(highlight(code, lexer, formatter))
    code_image = Image.open(image_bytes)

    # code_image.save('code.png', 'png')
    return code_image
