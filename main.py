from matchmaker import Matchmaker
from team import Team

def setup_matchmaker_teams(matchmaker: Matchmaker) -> Matchmaker:
	matchmaker \
		.add_team(Team(name='PSG', 				pot_id=0)) \
		.add_team(Team(name='RB Leipzig', 		pot_id=0)) \
		.add_team(Team(name='Real Madrid', 		pot_id=0)) \
		.add_team(Team(name='Manchester City', 	pot_id=0)) \
		.add_team(Team(name='Liverpool', 		pot_id=0)) \
		.add_team(Team(name='Inter', 			pot_id=0)) \
		.add_team(Team(name='Borussia Dortmund', pot_id=0)) \
		.add_team(Team(name='Bayern Munich', 	pot_id=0)) \
		.add_team(Team(name='FC Barcelona', 	pot_id=0)) \
		.add_team(Team(name='Club Brugge', 		pot_id=1)) \
		.add_team(Team(name='Shakhtar Donetsk', pot_id=1)) \
		.add_team(Team(name='AC Milan', 		pot_id=1)) \
		.add_team(Team(name='Arsenal', 			pot_id=1)) \
		.add_team(Team(name='Juventus', 		pot_id=1)) \
		.add_team(Team(name='Atalanta', 		pot_id=1)) \
		.add_team(Team(name='Atlético Madrid', 	pot_id=1)) \
		.add_team(Team(name='Bayer Leverkusen', pot_id=1)) \
		.add_team(Team(name='Benfica', 			pot_id=1)) \
		.add_team(Team(name='Dinamo Zagreb', 	pot_id=2)) \
		.add_team(Team(name='Slavia Praga', 	pot_id=2)) \
		.add_team(Team(name='Rangers', 			pot_id=2)) \
		.add_team(Team(name='Celtic', 			pot_id=2)) \
		.add_team(Team(name='Aston Villa', 		pot_id=2)) \
		.add_team(Team(name='AS Monaco', 		pot_id=2)) \
		.add_team(Team(name='Sporting CP', 		pot_id=2)) \
		.add_team(Team(name='PSV', 				pot_id=2)) \
		.add_team(Team(name='Feyenord', 		pot_id=2)) \
		.add_team(Team(name='Girona FC', 		pot_id=3)) \
		.add_team(Team(name='Bologna', 			pot_id=3)) \
		.add_team(Team(name='Sturm Graz', 		pot_id=3)) \
		.add_team(Team(name='VFB Stuttgart', 	pot_id=3)) \
		.add_team(Team(name='Slovan Bratislava', pot_id=3)) \
		.add_team(Team(name='Brest', 			pot_id=3)) \
		.add_team(Team(name='Jagiellonia', 		pot_id=3)) \
		.add_team(Team(name='Malmo', 			pot_id=3)) \
		.add_team(Team(name='Sparta Barłogi', 	pot_id=3))
	return matchmaker

def main() -> None:
    matchmaker = Matchmaker()
    matchmaker = setup_matchmaker_teams(matchmaker)

    MATCHES_PER_TEAM = 3

    for _ in range(MATCHES_PER_TEAM):
        matchmaker.reset_available_team_pool()

        while True:
            try:
                games = matchmaker.generate_game()
                for game in games:
                    print(f'{game.team_a.name} vs. {game.team_b.name}')
                break  # Exit loop if successful
            except Exception as e:
                print(f'Error generating games: {e}')

if __name__ == '__main__':
	main()
