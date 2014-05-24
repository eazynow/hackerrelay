import requests


def main():
	r = requests.get("http://hacker-olympics-london.herokuapp.com/leaderboard.json")

	leaderboard = r.json()

	r.close()

	print "Base version"
	print "With erols addition & Dans & Deborah"
    print "Superior code added be Telecoda"
    print "and with a fix from Janusz"

	for place in leaderboard.keys():
		if leaderboard[place]["name"] == "Skaro":
			print "we have %d points" % leaderboard[place]["points"]

if __name__ == "__main__":
    main()
