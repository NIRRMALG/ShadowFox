Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
firstcity=input("enter first city name:")
secondcity=input("enter second city name:")
if firstcity in Australia and secondcity in Australia:
    print(f"Both cities are in Australia")
elif firstcity in UAE and secondcity in UAE:
    print(f"Both cities are in UAE")
elif firstcity in India and secondcity in India:
    print(f"Both cities are in India")
else:
    print(f"They dont belong to same countries")
