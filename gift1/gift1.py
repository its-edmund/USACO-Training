class gift1:
    def __init__(self):
        self.input = open("gift1.in", "r")
        self.output = open("gift1.out", "w")
        self.lines = self.input.readlines()
        self.numPeople = int(self.lines.pop(0))
        self.people = {}
        for i in range(0, self.numPeople):
            self.people[self.lines.pop(0).strip()] = 0

    def giveGifts(self):
        for i in range(0, len(self.people)):
            personName = self.lines.pop(0)
            info = self.lines.pop(0).split()
            money = int(info[0])
            numOfPeople = int(info[1])
            if numOfPeople == 0:
                break
            givenMoney = money // numOfPeople
            leftOverMoney = money % numOfPeople
            for i in range(0, numOfPeople):
                personGiven = self.lines.pop(0).strip()
                self.people[personGiven] = self.people[personGiven] + givenMoney
            self.people[personName.strip()] = self.people[personName.strip()] - money + leftOverMoney
        self.writeGifts()

    def printGifts(self):
        print(self.people)

    def writeGifts(self):
        for person in self.people:
            self.output.write(person + " " + str(self.people[person]) + "\n")

def main():
    gifts = gift1()
    gifts.giveGifts()

if __name__ == "__main__":
    main()