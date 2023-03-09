from team import Team
import unittest

class testTeam(unittest.TestCase):
   def test_type(self):
      team1 = Team()
      team1.name = "Redbacks"
      team1.wins = 99
      team1.losses = 10
      self.assertEqual(type(team1.get_win_percentage()) , type(0.0)) 



if __name__ == "__main__":
   unittest.main()
