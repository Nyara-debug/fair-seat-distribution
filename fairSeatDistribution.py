import math

parties = input("Enter parties: ").replace(" ", "").split(",")
votes = input("Enter votes: ").replace(" ", "").split(",")
seats = int(input("Number of seats: "))
percentageOfVotes = []
baseSeats = []
endSeats = []
baseWeight = []
weight = []

allvotes = 0
for i in votes:
    allvotes += int(i)

for i in range(len(votes)):
    percentageOfVotes.append(int(votes[i])/allvotes)
    baseSeats.append(int(math.floor(seats*percentageOfVotes[i])))
    baseWeight.append(float(baseSeats[i]/(seats*percentageOfVotes[i])))

givenSeats = 0
endSeats = baseSeats
endWeight = baseWeight
for i in baseSeats:
    givenSeats += i

while seats - givenSeats != 0:
    avWght = 1000
    for i in range(len(votes)):
        endSeats[i] = int(endSeats[i]) + 1
        oldWeight = endWeight[i]
        endWeight[i] = int(endSeats[i])/(seats*float(percentageOfVotes[i]))
        newAvg = 0
        partiesWithSeats = 0
        for j in range(len(endWeight)):
            #newAvg *= float(endWeight[j])
            newAvg = newAvg + float(abs(1 - (endWeight[j])))
            if int(endSeats[j]) > 0:
                partiesWithSeats += 1
        newAvg = newAvg/partiesWithSeats
        if abs(avWght) > abs(newAvg):
            avWght = newAvg
            x = i
        endSeats[i] = int(endSeats[i]) - 1
        endWeight[i] = oldWeight
    endSeats[x] = int(endSeats[x]) + 1
    endWeight[x] = int(endSeats[x])/(seats*float(percentageOfVotes[x]))
    givenSeats += 1
    
lenpart = 0
lenseat = 0
for i in range(len(parties)):
    if lenpart < len(parties[i]):
        lenpart = len(parties[i])
    if lenseat < len(str(endSeats[i])):
        lenseat = len(str(endSeats[i]))
        
for i in range(len(parties)):
    print('{:^{}}'.format(parties[i], lenpart), "  |  ", '{:^{}}'.format(endSeats[i], lenseat), "  |  ", endWeight[i])

    


        
