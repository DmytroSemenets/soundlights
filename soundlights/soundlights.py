import sys
from neopixel import Adafruit_NeoPixel, Color

# LED strip configuration:
LED_COUNT = 60  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False # True to invert the signal (when using NPN transistor level shift)

# Colors:
COLORS_COUNT = 256
COLORS_OFFSET = 50


def _get_strip():
    strip = Adafruit_NeoPixel(
        LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

    strip.begin()

    for i in range(0, strip.numPixels(), 1):
        strip.setPixelColor(i, Color(0, 0, 0))

    strip.setBrightness(100)

    return strip


def _get_spaced_colors(n):
    max_value = 16581375
    interval = int(max_value / n)
    colors = [hex(i)[2:].zfill(6) for i in range(0, max_value, interval)]

    return [(int(i[:2], 16), int(i[2:4], 16), int(i[4:], 16)) for i in colors]


def _handle_stdin(colors, strip):
    while True:
        try:
            nums = map(int, sys.stdin.readline()[:-1].split())
            for i, num in enumerate(nums):
                strip.setPixelColor(i, Color(*colors[num]))

            strip.show()
        except Exception as e:
            print e


if __name__ == '__main__':
    _handle_stdin(_get_spaced_colors(COLORS_COUNT),
                  _get_strip())
