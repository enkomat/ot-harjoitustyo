import importlib
from game_event import Game_Event

from level_solutions.level_1_solution import Level_1_Solution
from level_solutions.level_2_solution import Level_2_Solution
from level_solutions.level_3_solution import Level_3_Solution
from level_solutions.level_4_solution import Level_4_Solution
from level_solutions.level_5_solution import Level_5_Solution
from level_solutions.level_6_solution import Level_6_Solution

class Event_Handler:
    def __init__(self, util):
        self.util = util
        self.logic = self.util.logic
        self.event_list = []
        self.event_parameter_list = []
        self.event_execution_amount = 0
        self.time_since_last_event_execute = 0.0
        self.event_index = 0
        self.event_execution_speed = 120

    def execute_next_method_in_event_list(self):
        """Suorittaa seuraavan metodin pelin aikana suoritettavien metodien listasta.
        """
        if self.event_index < len(self.event_list) and self.time_since_last_event_execute > self.event_execution_speed:
            event_type = self.event_list[self.event_index]
            player_reference = self.event_parameter_list[self.event_index]
            if event_type is Game_Event.MOVE_PLAYER_RIGHT:
                self.logic.move_player_right(player_reference)
            elif event_type is Game_Event.MOVE_PLAYER_LEFT:
                self.logic.move_player_left(player_reference)
            elif event_type is Game_Event.MOVE_PLAYER_UP:
                self.logic.move_player_up(player_reference)
            elif event_type is Game_Event.MOVE_PLAYER_DOWN:
                self.logic.move_player_down(player_reference)
            elif event_type is Game_Event.PLAYER_INTERACT:
                self.logic.player_interact(player_reference)
            elif event_type is Game_Event.PLAYER_BUILD_WALL:
                self.logic.player_build_wall(player_reference)
            elif event_type is Game_Event.PLAYER_BUILD_DOOR:
                self.logic.player_build_door(player_reference)
            
            self.event_execution_amount += 1
            self.time_since_last_event_execute = 0.0
            self.event_index += 1

    def all_events_have_been_executed(self):
        return self.event_index == len(self.event_list)

    def reload_events(self, level_index):
        self.event_index = 0
        self.event_execution_amount = 0
        self.time_since_last_event_execute = 0.0
        
        if level_index == 0:
            self.reload_level_1_events()
        elif level_index == 1:
            self.reload_level_2_events()
        elif level_index == 2:
            self.reload_level_3_events()
        elif level_index == 3:
            self.reload_level_4_events()
        elif level_index == 4:
            self.reload_level_5_events()
        elif level_index == 5:
            self.reload_level_6_events()

    def reload_level_1_events(self):
        self.event_list.clear()
        self.event_parameter_list.clear()
        try:
            import level_solutions.level_1_solution 
            importlib.reload(level_solutions.level_1_solution)
            from level_solutions.level_1_solution  import Level_1_Solution
            self.util.solution = Level_1_Solution(self.util.level_util.level)
        except:
            print("Error with reloading your solution.")

    def reload_level_2_events(self):
        self.event_list.clear()
        self.event_parameter_list.clear()
        try:
            import level_solutions.level_2_solution 
            importlib.reload(level_solutions.level_2_solution)
            from level_solutions.level_2_solution import Level_2_Solution
            self.util.solution = Level_2_Solution(self.util.level_util.level)
        except:
            print("Error with reloading your solution.")

    def reload_level_3_events(self):
        self.event_list.clear()
        self.event_parameter_list.clear()
        try:
            import level_solutions.level_3_solution
            importlib.reload(level_solutions.level_3_solution)
            from level_solutions.level_3_solution import Level_3_Solution
            self.util.solution = Level_3_Solution(self.util.level_util.level)
        except:
            print("Error with reloading your solution.")

    def reload_level_4_events(self):
        self.event_list.clear()
        self.event_parameter_list.clear()
        try:
            import level_solutions.level_4_solution
            importlib.reload(level_solutions.level_4_solution)
            from level_solutions.level_4_solution import Level_4_Solution
            self.util.solution = Level_4_Solution(self.util.level_util.level)
        except:
            print("Error with reloading your solution.")

    def reload_level_5_events(self):
        self.event_list.clear()
        self.event_parameter_list.clear()
        try:
            import level_solutions.level_5_solution
            importlib.reload(level_solutions.level_5_solution)
            from level_solutions.level_5_solution import Level_5_Solution
            self.util.solution = Level_5_Solution(self.util.level_util.level)
        except:
            print("Error with reloading your solution.")

    def reload_level_6_events(self):
        self.event_list.clear()
        self.event_parameter_list.clear()
        try:
            import level_solutions.level_6_solution
            importlib.reload(level_solutions.level_6_solution)
            from level_solutions.level_6_solution import Level_6_Solution
            self.util.solution = Level_6_Solution(self.util.level_util.level)
            self.util.level_util.randomize_pillars()
        except:
            print("Error with reloading your solution.")

    def add_new_event(self, method_name, method_parameter):
        """Lisää tietyn metodikutsun suoritettavien metodien listaan, eli event_list listaan.

        Args:
            method_to_add (metodikutsu): Mikä tahansa metodi joka halutaan lisätä suoritettavien metodien listaan.
            parameter (metodikutsun parametrin): Aiemman metodin parametri jota tarvitaan.
        """
        self.event_list.append(method_name)
        self.event_parameter_list.append(method_parameter)