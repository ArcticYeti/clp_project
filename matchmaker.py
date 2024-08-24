from __future__ import annotations
from dataclasses import dataclass, field
import random

from game import Game
from team import Team


@dataclass
class Matchmaker:
	team_count: int = field(default=0, init=False)
	_all_teams: dict[str, Team] = field(default_factory=dict, init=False, repr=False)
	_available_team_pool: list[Team] = field(default_factory=list, init=False, repr=False)

	def add_team(self, team: Team) -> Matchmaker:
		self._all_teams[team.name] = team
		self.team_count += 1
		return self

	def reset_available_team_pool(self) -> Matchmaker:
		self._available_team_pool = list(self._all_teams.values())
		return self

	def generate_game(self) -> list[Game]:
		max_attempts = 100
		attempts = 0

		while attempts < max_attempts:
			random.shuffle(self._available_team_pool)
			games = []

			# Create games
			while len(self._available_team_pool) >= 2:
				# team_a = self._available_team_pool.pop(0)
				# team_b = self._available_team_pool.pop(0)
				team_a = self._available_team_pool[0]
				team_b = self._available_team_pool[0]

				if self._can_play(team_a, team_b):
					games.append(Game(team_a, team_b))
				else:
					self._available_team_pool.append(team_a)
					self._available_team_pool.append(team_b)

				if len(self._available_team_pool) < 2:
					random.shuffle(self._available_team_pool) 

			if len(games) == self.team_count // 2:
				return games

			attempts += 1
			self.reset_available_team_pool()

		raise Exception('Failed to generate a valid set of matches after maximum attempts!')

	def _can_play(self, team_a: Team, team_b: Team) -> bool:
		if team_a.already_played_against(team_b) or team_b.already_played_against(team_a):
			return False
		if team_a.pot_versing_count[team_b.pot_id] >= 2 or team_b.pot_versing_count[team_a.pot_id] >= 2:
			return False
		return True
