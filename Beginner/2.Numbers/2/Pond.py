radius=84
area=3.14*radius*radius
water_per_squaremetre=1400
water_in_pond=area*water_per_squaremetre
a,b=(water_in_pond//1000),(water_in_pond % 1000)
print(f"The area of the pond is {int(area)} square metre. If the water per squaremetre is 1 litre 400 millilitre then Total amount of water in pond is {int(a)} litre  and {int(b)} millilitre.")
