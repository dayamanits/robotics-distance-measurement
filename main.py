distance = float(input("Enter distance to obstacle in cm: "))

if distance <= 10:
    print("STOP! Obstacle very close!")
elif distance <= 30:
    print("WARNING! Obstacle nearby.")
else:
    print("Safe distance. Robot can move.")

