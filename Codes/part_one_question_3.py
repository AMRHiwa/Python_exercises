import math
wind_speed, temp = map(int, input("Enter speed and tempture: ").split() )

print(f"Wind Chill: {13.12 + 0.6215 * temp - 11.37 * math.pow(wind_speed, 0.16) + 0.3965 * temp * math.pow(wind_speed, 0.16)}")