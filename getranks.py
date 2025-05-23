import requests
import json

API_KEY = "RGAPI-c82def11-a28b-4157-96d1-4018e6d99f41"
region = "NA1"

class Summoner:
	
	def __init__(self, unencrypted_username: str, tagline: str):
		self.unencrypted_username = unencrypted_username
		self.tagline = tagline
		self.data = self.get_rank_info(self.get_encrypted_username(self.unencrypted_username)) #api key separate
		self.tier = self.data[0]['tier']
		self.rank = self.data[0]['rank']
		self.lp = self.data[0]['leaguePoints']	

	def get_encrypted_username(self, unencrypted_username: str) -> str:
		get_encrypted_username_url = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{unencrypted_username}/{self.tagline}?api_key={API_KEY}'
		headers = {'X-Riot-Token': API_KEY}
		response = requests.get(get_encrypted_username_url, headers=headers)
		if response.status_code == 200:
			data = response.json()
			encrypted_username  = data['puuid']
			return encrypted_username
		else:
			raise Exception( f'error: {response.status_code}')

	def get_rank_info(self, encrypted_username: str) -> str:
		get_summoner_info_url = f'https://na1.api.riotgames.com/lol/league/v4/entries/by-puuid/{encrypted_username}?api_key={API_KEY}'
		headers = {'X-Riot-Token': API_KEY}
		response = requests.get(get_summoner_info_url, headers=headers)

		if response.status_code == 200:
			data = response.json()
			tier = data[0]['tier']
			rank = data[0]['rank']
			lp = data[0]['leaguePoints']
			return data;
		else:
			raise Exception( f'error: {response.status_code}')

	def __lt__(self, other): #true if self is less than other
		tiers = ['IRON', 'SILVER', 'GOLD', 'PLATINUM', 'EMERALD', 'DIAMOND', 'MASTER', 'GRANDMASTER', 'CHALLENGER']
		ranks = ['IV', 'III', 'II', 'I']
		if self.tiers.index() < other.tiers.index():
			return True
		elif self.tiers.index() > other.tiers.index():
			return False
		else:
			if self.rank.index() < other.rank.index():
				return True
			elif self.rank.index() > other.rank.index():
				return False
			else:
				if self.lp < other.lp:
					return True
				else:
					False

	def __eq__(self, other):
		return self.tiers.index() == other.tiers.index() and self.rank.index() == other.rank.index() and self.lp == self.lp

	def __repr__(self):
		return f'{self.unencrypted_username}: {self.tier} {self.rank} {self.lp}lp'
