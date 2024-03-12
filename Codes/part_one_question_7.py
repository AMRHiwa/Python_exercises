# gettin R1, R2, R3
R1, R2, R3 = map(int, input("Enter R1, R2, R3: ").split())

# calculate R and showing in output
print(f"R: {((R1 * R2) + (R1 * R3) + (R2 * R3)) / (R1 * R2 * R3)}")