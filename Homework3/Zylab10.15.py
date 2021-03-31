# Justino Cortez ID 1615245

class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_team_name(self, team_name):
        self.team_name = team_name

    def get_team_wins(self, team_wins):
        self.team_wins = team_wins

    def get_team_losses(self, team_losses):
        self.team_losses = team_losses

    def get_win_percentage(self):
        win_percentage = self.team_wins / (self.team_wins + self.team_losses)
        return win_percentage


if __name__ == "__main__":

    team = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.get_team_name(team_name)
    team.get_team_wins(team_wins)
    team.get_team_losses(team_losses)

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.team_name, 'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')
