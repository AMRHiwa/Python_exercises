# getting initial speed , time and final speed
init_speed, time, final_speed = map(float, input("Enter intial speed, time and final speed : ").split())

# calculate R
print(f"R:{(final_speed + init_speed * 60) / time}")