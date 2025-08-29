import random
import time

import mouse

class Automovement():
    
    def __init__(self, absolute_ref):
        self.__running = True
        self.__mouse = mouse
        self.__absolute_ref = absolute_ref
        self.__mouse.on_right_click(self.__on_right_click)

    def __on_right_click(self) -> None:
        self.__running = False

    def __mouse_movement(self) -> None:
        self.__mouse.move(
            self.__next_targ_x,
            self.__next_targ_y,
            absolute=self.__absolute_ref,
            duration=self.__time
        )

    def __calculate_mouse_movement(self, min_val=200, max_val=800, t=(1, 3)) -> None:
        self.__next_targ_x = random.randint(min_val, max_val)
        self.__next_targ_y = random.randint(min_val, max_val)
        self.__time = random.randint(t[0], t[1])
        self.__mouse_movement()

    def __mouse_click(self) -> None:
        self.__calculate_mouse_movement(min_val=0, max_val=0, t=(1, 2))
        self.__mouse.click(button='left')

    def run(self):
        while self.__running:
            self.__calculate_mouse_movement()
            self.__mouse_click()
            time.sleep(3)