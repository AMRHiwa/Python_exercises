# getting radius and hieght
radius, hieght = map(float, input("Enter radius and hieght: ").split())

# cylinder volume
print(f'cylinder volume: {3.14*(radius**2)*hieght}')

# Lateral area of the cylinder
print(f'Lateral area of the cylinder: {(2*3.14*radius*hieght)+(2*3.14*(radius**2))}')