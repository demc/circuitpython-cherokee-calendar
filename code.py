import board
import terminalio
import displayio
from digitalio import DigitalInOut
from adafruit_display_text.label import Label
from adafruit_bitmap_font import bitmap_font
from adafruit_button import Button
from waveshare_res_touch import WaveshareResTouch, LANDSCAPE
from random import randint


# Load the syllabary
syllabary = 'ᎠᎡᎢᎣᎤᎥᎦᎧᎨᎩᎪᎫᎬᎭᎮᎯᎰᎱᎲᎳᎴᎵᎶᎷᎸᎹᎺᎻᎼᎽᎾᎿᏀᏁᏂᏃᏄᏅᏆᏇᏈᏉᏊᏋᏌᏍᏎᏏᏐᏑᏒᏓᏔᏕᏖᏗᏘᏙᏚᏛᏜᏝᏞᏟᏠᏡᏢᏣᏤᏥᏦᏧᏨᏩᏪᏫᏬᏭᏮᏯᏰᏱᏲᏳᏴᏵᏸᏹᏺᏻᏼᏽ'
# cherokee = bitmap_font.load_font('/fonts/NotoSansCherokee-Regular-24.bdf')
cherokee = bitmap_font.load_font('/fonts/NotoSansCherokee-Regular-10.bdf')


# Preload the glyphs from the syllabary that will actually be rendered.
preloaded_glyphs = syllabary
print('Preloading these glyphs', preloaded_glyphs)
cherokee.load_glyphs(preloaded_glyphs)

numerals = '0123456789'
cherokee_numerals = bitmap_font.load_font('/fonts/Cherokee-Numerals.bdf')

print('Preloading numeral glyphs', numerals)
cherokee_numerals.load_glyphs(numerals)

# Release any resources currently in use for the displays.
displayio.release_displays()

# Setup the Waveshare Pico ResTouch screen.
TFT_WIDTH = 320
TFT_HEIGHT = 240
ORIENTATION = LANDSCAPE
waveshare = WaveshareResTouch(width=TFT_WIDTH, height=TFT_HEIGHT, orientation=ORIENTATION)

# Setup the display object.
display = waveshare.DISPLAY
root = displayio.Group()
display.show(root)

n = ord('a')
print(n)
print(terminalio.FONT.get_glyph(n))


# Cherokee Sunday
sun = Label(
    anchor_point=(0, 0),
    anchored_position=(1, 0),
    scale=1,
    line_spacing=0.7,
    text='ᏙᏓᏆ\nᏍᎬᎢ',
    font=cherokee,
    color=0xffffff,
)
root.append(sun)

# English Monday
# mon = Label(
#     anchor_point=(0, 0),
#     anchored_position=(48, -7),
#     scale=2,
#     text='Mon',
#     font=terminalio.FONT,
#     color=0xffffff,
# )
# root.append(mon)
# Cherokee Monday
mon = Label(
    anchor_point=(0, 0),
    anchored_position=(48, 0),
    scale=1,
    line_spacing=0.7,
    text='ᏙᏓᏉ\nᏅᎢ',
    font=cherokee,
    color=0xffffff,
)
root.append(mon)

# English Tuesday
# tue = Label(
#     anchor_point=(0, 0),
#     anchored_position=(95, -7),
#     scale=2,
#     text='Tue',
#     font=terminalio.FONT,
#     color=0xffffff,
# )
# root.append(tue)
tue = Label(
    anchor_point=(0, 0),
    anchored_position=(95, 0),
    scale=1,
    line_spacing=0.7,
    text='ᏔᎵ\nᏁᎢᎦ',
    font=cherokee,
    color=0xffffff,
)
root.append(tue)

# English Wednesday
# wed = Label(
#     anchor_point=(0, 0),
#     anchored_position=(142, -7),
#     scale=2,
#     text='Wed',
#     font=terminalio.FONT,
#     color=0xffffff,
# )
# root.append(wed)
# Cherokee Wednesday
wed = Label(
    anchor_point=(0, 0),
    anchored_position=(142, 0),
    scale=1,
    line_spacing=0.7,
    text='ᏦᎢ\nᏁᎢᎦ',
    font=cherokee,
    color=0xffffff,
)
root.append(wed)

# English Thursday
# thu = Label(
#     anchor_point=(0, 0),
#     anchored_position=(189, -7),
#     scale=2,
#     text='Thu',
#     font=terminalio.FONT,
#     color=0xffffff,
# )
# root.append(thu)
# Cherokee Thursday
thu = Label(
    anchor_point=(0, 0),
    anchored_position=(189, 0),
    scale=1,
    line_spacing=0.7,
    text='ᏅᎩ\nᏁᎢᎦ',
    font=cherokee,
    color=0xffffff,
)
root.append(thu)

# English Friday
# fri = Label(
#     anchor_point=(0, 0),
#     anchored_position=(236, -7),
#     scale=2,
#     text='Fri',
#     font=terminalio.FONT,
#     color=0xffffff,
# )
# root.append(fri)
# Cherokee Friday
fri = Label(
    anchor_point=(0, 0),
    anchored_position=(236, 0),
    scale=1,
    line_spacing=0.7,
    text='ᏧᏅᎩ\nᎶᏍᏗ',
    font=cherokee,
    color=0xffffff,
)
root.append(fri)

# Enlgish Saturday
# sat = Label(
#     anchor_point=(0, 0),
#     anchored_position=(283, -7),
#     scale=2,
#     text='Sat',
#     font=terminalio.FONT,
#     color=0xffffff,
# )
# root.append(sat)
# Cherokee Saturday
sat = Label(
    anchor_point=(0, 0),
    anchored_position=(283, 0),
    scale=1,
    line_spacing=0.7,
    text='ᏙᏓ\nᏈᏕᎾ',
    font=cherokee,
    color=0xffffff,
)
root.append(sat)

# one = Label(
#     anchor_point=(0, 0),
#     anchored_position=(1, 20),
#     scale=2,
#     text='1',
#     font=cherokee_numerals,
#     color=0xffffff,
# )
# root.append(one)
# 
# two = Label(
#     anchor_point=(0, 0),
#     anchored_position=(48, 20),
#     scale=2,
#     text='2',
#     font=cherokee_numerals,
#     color=0xffffff,
# )
# root.append(two)
# 
# three = Label(
#     anchor_point=(0, 0),
#     anchored_position=(95, 20),
#     scale=2,
#     text='3',
#     font=cherokee_numerals,
#     color=0xffffff,
# )
# root.append(three)
# 
# four = Label(
#     anchor_point=(0, 0),
#     anchored_position=(142, 20),
#     scale=2,
#     text='4',
#     font=cherokee_numerals,
#     color=0xffffff,
# )
# root.append(four)
# 
# five = Label(
#     anchor_point=(0, 0),
#     anchored_position=(187, 20),
#     scale=2,
#     text='5',
#     font=cherokee_numerals,
#     color=0xffffff,
# )
# root.append(five)
# 
# six = Label(
#     anchor_point=(0, 0),
#     anchored_position=(234, 20),
#     scale=2,
#     text='6',
#     font=cherokee_numerals,
#     color=0xffffff,
# )
# root.append(six)
# 
# seven = Label(
#     anchor_point=(0, 0),
#     anchored_position=(281, 20),
#     scale=2,
#     text='7',
#     font=cherokee_numerals,
#     color=0xffffff,
# )
# root.append(seven)
# 
# seventy_seven = Label(
#     anchor_point=(0, 0),
#     anchored_position=(1, 60),
#     scale=1,
#     text='77',
#     font=cherokee_numerals,
#     color=0xffffff,
# )
# root.append(seventy_seven)