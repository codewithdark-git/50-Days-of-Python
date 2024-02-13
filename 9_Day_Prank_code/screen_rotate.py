
# auto rptate_screen when run program
import rotatescreen
import time

screen = rotatescreen.get_primary_display()
start_pos = screen.current_orientation


for i in range(1, 5):
    pos = abs((start_pos - i * 90) % 360)
    screen.rotate_to(pos)
    time.sleep(0.10)


# program run and user click button then rotate
# import rotatescreen
# import keyboard
#
# screen = rotatescreen.get_primary_display()
#
# keyboard.add_hotkey('ctrl+alt+up', screen.set_landscape, suppress=True)
# keyboard.add_hotkey('ctrl+alt+right', screen.set_portrait_flipped, suppress=True)
# keyboard.add_hotkey('ctrl+alt+down', screen.set_landscape_flipped, suppress=True)
# keyboard.add_hotkey('ctrl+alt+left', screen.set_portrait, suppress=True)
#
# keyboard.wait()