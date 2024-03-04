import random
import subprocess
import time

import keyboard
import mouse

class MyBreak():
    
    def __init__(self):
        self.__teams = 0
        self.__get_pid_teams()
        self.__running = True
        self.__absolute_ref = True
        self.__mouse = mouse
        self.__next_targ_x = 50
        self.__next_targ_y = 50
        self.__time = 2

    def run(self):
        while self.__running:
            self.__mouse.move(self.__next_targ_x, self.__next_targ_y ,absolute=self.__absolute_ref, duration=self.__time)
            self.__calculate_mouse_movement()
            self.__running = self.__simulate_process()
            
    def __calculate_mouse_movement(self) -> None:
        self.__time = random.randint(1,2)
        self.__next_targ_x = random.randint(50,600)
        self.__next_targ_y = random.randint(50,600)

    def __simulate_process(self) -> bool:
        self.__teams = subprocess.Popen("ms-teams.exe")
        self.__teams = self.__teams.pid
        for _ in range(30):
            time.sleep(1)
            if keyboard.is_pressed("Esc"):
                return False
        self.__kill_process()
        return True
    
    def __get_pid_teams(self):
        self.__teams = subprocess.Popen(['powershell.exe', 'Get-Process | Where-Object { $_.ProcessName -eq "ms-teams" } | ForEach-Object { $_.Id }'], stdout=subprocess.PIPE)
        out, _ = self.__teams.communicate()
        index = str(out).index("\\")
        self.__teams = int(str(out)[2:index])
        time.sleep(2)
        if self.__teams:
            self.__kill_process()
    
    def __kill_process(self):
        subprocess.check_output("Taskkill /PID %d /F" % self.__teams)

        