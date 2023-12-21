vehicles = {'Bicycle','Scooter','Car','Bike','Truck','Bus','Rickshaw'}
heavyVehicles = {'Truck','Bus'}
lightVehicles = {'Rickshaw','Scooter','Bike','Bicycle'}

#1
lytVehicles=vehicles-heavyVehicles
print(lytVehicles)
# Output : {'Bicycle', 'Scooter', 'Bike', 'Car', 'Rickshaw'}

#2
hvyVehicles = vehicles - lightVehicles
#print(hvyVehicles)
# Output : {'Car', 'Bus', 'Truck'}

#3
averageWeightVehicles = lytVehicles & hvyVehicles
#print(averageWeightVehicles)
# Output : {'Car'}

#4
transport = lightVehicles | heavyVehicles
#print(transport)
# Output : {'Scooter', 'Truck', 'Bicycle', 'Bike', 'Rickshaw', 'Bus'}

#5
transport.add('Car')
#print(transport)
# Output : {'Scooter', 'Car', 'Truck', 'Bicycle', 'Bike', 'Rickshaw', 'Bus'}

#6
#for i in vehicles:
#    print(i)
# Output : Bicycle
#          Scooter
#          Truck
#          Bus
#          Car
#          Rickshaw
#          Bike


#7
#print(len(vehicles))
# Output : 7

#8
#print(min(vehicles))
# Output : Bicycle

#9
#print(set.union(vehicles, lightVehicles, heavyVehicles))
#Output : {'Bus', 'Truck', 'Car', 'Bike', 'Scooter', 'Bicycle', 'Rickshaw'}

