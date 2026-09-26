# Smart Street Light using Python

def smart_street_light(light_level, motion):
print("\n===== SMART STREET LIGHT =====")
print(f"Light Level : {light_level}%")
print(f"Motion      : {motion}")

```
# Low light + motion detected
if light_level < 30 and motion == "yes":
    print("Condition: Dark + Motion Detected")
    print("Street Light: ON")
    print("Brightness: 100%")

# Low light but no motion
elif light_level < 30 and motion == "no":
    print("Condition: Dark + No Motion")
    print("Street Light: ON")
    print("Brightness: 30%")

# Daylight
else:
    print("Condition: Sufficient Light")
    print("Street Light: OFF")
```

while True:
print("\n1. Check Street Light")
print("2. Exit")

```
choice = input("Enter your choice: ")

if choice == "1":
    try:
        light_level = float(
            input("Enter light level (0-100%): ")
        )

        motion = input(
            "Is motion detected? (yes/no): "
        ).lower()

        if 0 <= light_level <= 100 and motion in ["yes", "no"]:
            smart_street_light(light_level, motion)
        else:
            print("Enter valid values.")

    except ValueError:
        print("Invalid input! Enter a number for light level.")

elif choice == "2":
    print("Smart Street Light System Closed.")
    break

else:
    print("Invalid choice! Please try again.")
```
