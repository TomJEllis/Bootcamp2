from Lab_12_16_win_team import Team
 
student_team = Team()
student_team.team_wins = 13
student_team.team_losses= 3
 
student_win_percentage = student_team.get_win_percentage()

perc_times_100 = int(student_team.get_win_percentage() * 100)

if perc_times_100 == int(0.8125 * 100):
    print("\nTEST PASSED:\nWin percentage 0.8125 (81.25%) correctly returned.\n") 
else:
    print(f"\nTEST FAILED:\nIncorrect win percentage {student_team.get_win_percentage()} returned\n") 

