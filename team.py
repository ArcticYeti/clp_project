from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Team:
	name: str = field(kw_only=True)
	pot_id: int = field(kw_only=True)

	pot_versing_count: list[int] = field(default_factory=list, init=False, repr=False)
	_already_played_against: list[Team] = field(default_factory=list, init=False, repr=False)
	
	def __post_init__(self):
		self.pot_versing_count = [0, 0, 0, 0]
	
	def already_played_against(self, opponent: Team) -> bool:
		return opponent in self._already_played_against

	def register_opponent(self, opponent: Team):
		self.pot_versing_count[opponent.pot_id] += 1
		self._already_played_against.append(opponent)
