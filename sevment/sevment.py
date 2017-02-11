import time

from Adafruit_LED_Backpack import SevenSegment

hex_crosswalk = {
  "0": 0x7E,
  "1": 0x30,
  "2": 0x6D,
  "3": 0x79,
  "4": 0x33,
  "5": 0x5B,
  "6": 0x5F,
  "7": 0x70,
  "8": 0x7F,
  "9": 0x7B,
  " ": 0x00,
  "A": 0x77,
  "a": 0x7D,
  "B": 0x7F,
  "b": 0x1F,
  "C": 0x4E,
  "c": 0x0D,
  "D": 0x7E,
  "d": 0x3D,
  "E": 0x4F,
  "e": 0x6f,
  "F": 0x47,
  "f": 0x47,
  "G": 0x5E,
  "g": 0x7B,
  "H": 0x37,
  "h": 0x17,
  "I": 0x30,
  "i": 0x10,
  "J": 0x3C,
  "j": 0x38,
  "K": 0x37,
  "k": 0x17,
  "L": 0x38,
  "l": 0x06,
  "M": 0x55,
  "m": 0x55,
  "N": 0x15,
  "n": 0x15,
  "O": 0x3F,
  "o": 0x1D,
  "P": 0x67,
  "p": 0x67,
  "Q": 0x73,
  "q": 0x73,
  "R": 0x77,
  "r": 0x05,
  "S": 0x5B,
  "s": 0x5B,
  "T": 0x46,
  "t": 0x0F,
  "U": 0x3E,
  "u": 0x1C,
  "V": 0x27,
  "v": 0x23,
  "W": 0x3F,
  "w": 0x2B,
  "X": 0x25,
  "x": 0x25,
  "Y": 0x3B,
  "y": 0x33,
  "Z": 0x6D,
  "z": 0x6D,
}

display = SevenSegment.SevenSegment()

# Initialize the display. Must be called once before using the display.
display.begin()

def countdown():
    for i in range(0,100):
        display.clear()
        display.print_float(i, decimal_digits=0)
        display.write_display()
        time.sleep(0.001)

    display.clear()

def spinner(hexadecimals):
    for i in hexadecimals:
        for e in range(0,4):
            display.set_digit_raw(e,i)
        display.write_display()
        time.sleep(0.03)
        display.clear()

    cleanup()

def scroll_message(message):

    message_hex = []
    for i in list(message):
        message_hex.append(hex_crosswalk.get(i))

    blanks = [0x00,0x00,0x00]
    final = blanks + message_hex + blanks

    while len(final)>3:
      fill_display(final[:4])
      final.pop(0)

    cleanup()

def cleanup():

    display.clear()
    display.write_display()

def fill_display(letters):
    display.clear()
    pos = 0
    for i in letters:
        display.set_digit_raw(pos,i)
        pos += 1
    display.write_display()
    time.sleep(0.3)

if __name__ == '__main__':
    for i in range(0,10):
        spinner([0x1,0x20,0x10,0x8,0x4,0x2])
    for i in range(0,10):
        spinner([0x8,0x40,0x1])
    for i in range(0,4):
        scroll_message('3L I LOU3 U')
    for i in range(0,10):
        spinner([0x1,0x20,0x10,0x8,0x4,0x2])
