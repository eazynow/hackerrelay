import requests


def main():
	r = requests.get("http://hacker-olympics-london.herokuapp.com/leaderboard.json")

	leaderboard = r.json()

	r.close()

	print "Base version"

	for place in leaderboard.keys():
		print leaderboard[place]["name"]

if __name__ == "__main__":
    main()
