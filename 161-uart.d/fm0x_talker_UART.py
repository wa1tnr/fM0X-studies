# simple UART output - sends a message to the far side.

# nis 23 Jan 2018  03:28 UTC or later.  03:29z at the moment.

from digitalio import DigitalInOut, Direction
import board
import busio
import time

print("acf32ecbb")

uart = busio.UART(board.TX, board.RX, baudrate=38400) # faster seems to improve signal to noise ratio

def emit():
    # buf = bytearray(26)        # a buffer to write to the UART
    buf = bytearray(444)       # a buffer to write to the UART
    # buf = str(" Pew Pew Pew Pew Pew Pew Pew Pew")
    # buf = str("Lorem ipsum dolor sit amet")
    buf = str("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum")
    uart.write(buf)
    buf = str("            lmnop        ")
    uart.write(buf)
    buf = str('\n'); uart.write(buf)
    buf = str('\n'); uart.write(buf)
    buf = str('\n'); uart.write(buf)
    buf = str('\n'); uart.write(buf)


print(" ")
print("Talking out the UART from Feather M0 Express.")
print(" ")
print("Look at the serial terminal connected to the far end")
print("of this conversation, for what I emit to the local UART.")

while True:
    emit()      # talking
    time.sleep(11.5) # does not improve on the noise

# END.
