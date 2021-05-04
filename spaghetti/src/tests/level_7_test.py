import unittest
import pygame
import math
from util import Level_7, Util_Level_7, Util

class TestLevel_7(unittest.TestCase):
    def test_solve_level(self):
        for i in range(3): # try thrice to be sure
            lvl7 = Level_7()
            util_lvl_7 = lvl7._Level_7__util_level_7
            self.solve_level(lvl7, util_lvl_7)
            util_lvl_7.run(True)
            self.assertEqual(util_lvl_7.level_failed, False)

    def solve_level(self, lvl7, util):
        # get biggest distance between two players
        biggest_dist = 0
        leader1 = lvl7.players[0]
        leader2 = lvl7.players[0]
        for player1 in lvl7.players:
            player1_xy = [player1.get_position_x(), player1.get_position_y()]
            for player2 in lvl7.players:
                if player1 == player2:
                    continue
                player2_xy = [player2.get_position_x(), player2.get_position_y()]
                dist = util.dist(player1_xy, player2_xy)
                if(dist > biggest_dist):
                    biggest_dist = dist
                    leader1 = player1
                    leader2 = player2

        # group 1
        leader1_xy = [leader1.get_position_x(), leader1.get_position_y()]
        distances = []
        players_grp1 = []
        for player in lvl7.players:
            if player == leader1:
                continue

            player_xy = [player.get_position_x(), player.get_position_y()]
            dist = util.dist(leader1_xy, player_xy)
            distances.append(dist)
            players_grp1.append(player)

        zipped_pairs = zip(distances, players_grp1)
        sorted_players = sorted(zipped_pairs, key = lambda x: x[0])

        group1 = [leader1]
        for i in range(7):
            group1.append(sorted_players[i][1])

        for player in group1:
            dist_x = abs(player.get_position_x() - 10)
            dist_y = abs(player.get_position_y() - 15)
            
            for i in range(dist_x):
                if player.get_position_x() > 10:        
                    player.move_left()
                else:
                    player.move_right()
            
            for i in range(dist_y):
                if player.get_position_y() > 15:        
                    player.move_up()
                else:
                    player.move_down()

            player.interact()

        # group 2
        for player in lvl7.players:
            if player in group1:
                continue

            dist_x = abs(player.get_position_x() - 20)
            dist_y = abs(player.get_position_y() - 15)
            
            for i in range(dist_x):
                if player.get_position_x() > 20:        
                    player.move_left()
                else:
                    player.move_right()
            
            for i in range(dist_y):
                if player.get_position_y() > 15:        
                    player.move_up()
                else:
                    player.move_down()

            player.interact()