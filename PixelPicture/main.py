from PIL import Image
from PIL import ImageDraw
from font_info import get_char_info


def init():
    bg_color = (67, 26, 80)
    word_color = (255, 255, 255)
    shadow_color = (191, 55, 241)
    word = 'asteria>'
    return bg_color, word_color, shadow_color, word


def generate_img(bg_color, word_color, shadow_color, word):
    GRID_PIXELS = 20
    x_start = 250
    y_start = 100

    image = Image.new('RGB', (1080, 360), bg_color)
    draw = ImageDraw.Draw(image)

    for every_char in word:
        char_info = get_char_info(every_char)
        x_now = x_start
        y_now = y_start
        for row_info in char_info:
            for color in row_info:
                if color == 0:
                    now_color = bg_color
                elif color == 1:
                    now_color = word_color
                else:
                    now_color = shadow_color
                draw.rectangle(((x_now, y_now), (x_now + GRID_PIXELS, y_now + GRID_PIXELS)), now_color)
                x_now += GRID_PIXELS
            x_now = x_start
            y_now += GRID_PIXELS
        x_start += len(char_info[0]) * GRID_PIXELS

    image.show()
    image.save('output.png')
    return


def main():
    bg_color, word_color, shadow_color, word = init()
    generate_img(bg_color, word_color, shadow_color, word)


if __name__ == '__main__':
    main()
