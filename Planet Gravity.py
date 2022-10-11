SolarSystem_planet=["Sun","Mercury","Venus","Earth","Moon","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"]
planet_gravity=[274,3.7,8.87,9.807,1.62,3.721,24.79,10.44,8.69,11.15,0.62]

print('Welcome to Explore the Planet - CECS 174 Edition!')

player_planet=str(input('Enter the planet you are jumping on: '))
player_planet=player_planet.capitalize()
if player_planet in SolarSystem_planet:
    answer=True
else:
    answer=False
while answer==False:
    print('Your planet is invalid, try again!')
    player_planet = str(input('Enter the planet you are jumping on: '))
    if player_planet in SolarSystem_planet:
        answer = True
    else:
        answer = False
compare_planet=str(input('Enter the planet you want to compare to: '))
compare_planet=compare_planet.capitalize()
if compare_planet in SolarSystem_planet:

    answer=True
else:
    answer=False
while answer==False:
    print('Your planet is invalid, try again!')
    compare_planet = str(input('Enter the planet you are jumping on: '))
    if compare_planet in SolarSystem_planet:
        answer = True
    else:
        answer = False

player_height=float(input('How high can you jump? '))
unit=str(input('Enter your unit: '))
def calculation(player_gravity,compare_gravity):
    percent=player_gravity/compare_gravity
    final_height=player_height*percent
    return final_height
player_planet_index=SolarSystem_planet.index(player_planet)
player_gravity=planet_gravity[player_planet_index]
compare_planet_index=SolarSystem_planet.index(compare_planet)
compare_gravity=planet_gravity[compare_planet_index]
final_height=f'{calculation(player_gravity,compare_gravity):.2f}'
print('On',compare_planet+', you can jump',final_height,unit)