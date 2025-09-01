import random
import time

from pynput.mouse import Button, Controller, Listener

class Automovement():
    
    def __init__(self):
        self.__running = True
        self.__mouse = Controller()
        self.__steps = 100

    def __on_right_click(self, x, y, button, pressed) -> None:
        if button == Button.right and pressed:
            self.__running = False

    def __mouse_movement(self) -> None:
        start_x, start_y = self.__mouse.position
        dx = (self.__next_targ_x - start_x) / self.__steps
        dy = (self.__next_targ_y - start_y) / self.__steps
        dt = self.__time / self.__steps
    
        for _ in range(self.__steps):
            self.__mouse.move(dx, dy)
            time.sleep(dt)

    def __calculate_mouse_movement(self, min_val=200, max_val=800, t=(1, 3)) -> None:
        self.__next_targ_x = random.randint(min_val, max_val)
        self.__next_targ_y = random.randint(min_val, max_val)
        self.__time = random.randint(t[0], t[1])
        self.__mouse_movement()

    def __mouse_click(self) -> None:
        self.__calculate_mouse_movement(min_val=0, max_val=0, t=(1, 2))
        self.__mouse.click(Button.left, 1)

    def run(self):
        listener = Listener(
            on_click=self.__on_right_click)
        listener.start()

        while self.__running:
            self.__calculate_mouse_movement()
            self.__mouse_click()
            time.sleep(3)