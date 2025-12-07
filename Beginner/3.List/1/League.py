justice_league = ["Superman","Batman","WonderWoman","Flash","Aquaman","Green Lantern"]

a=len(justice_league) #1 Calculate the number of members in the Justice League.
print("Initially:",justice_league)
print("number of members in the Justice League:",a)

justice_league+=["Batgirl","Nightwing"] #2. Batman recruited Batgirl and Nightwing as new members.Add them to your list
print("After Batman recruitment:",justice_league)

justice_league.remove("WonderWoman")  #3. Wonder Woman is now the leader of the Justice League.Move her to the beginning of the list.
justice_league.insert(0,"WonderWoman")
print("After Wonderwoman becoming the leader:",justice_league)

justice_league.remove("Green Lantern") #4. Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman"and move them in between Aquaman and Flash.
justice_league.insert(4,"Green Lanterns")
print("After solving the conflict:" ,justice_league)

justice_league=["Cyborg","Shazam","Hawkgirl","MartianManhunter","Green Arrow"] #5. The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with the following new members: "Cyborg""Shazam","Hawkgirl","MartianManhunter","Green Arrow".
print("After justice league faced the crisis:", justice_league)

justice_league.sort() #6. Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.
print("After sorting justice league alphabetically: ",justice_league)

print("The cureent leader:",justice_league[0])
