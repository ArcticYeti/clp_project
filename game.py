from dataclasses import dataclass

from team import Team

@dataclass
class Game:
	team_a: Team
	team_b: Team

	def __post_init__(self):
		self.team_a.register_opponent(self.team_b)
		self.team_b.register_opponent(self.team_a)
