# Ask the user for the fleet formation height
formation_height = int(input("Formation height (2-20): "))

# Validate the input
while formation_height < 2 or formation_height > 20:
    print("Formation height must be between 2 and 20.")
    formation_height = int(input("Formation height (2-20): "))

saucer = "<^>"
alien = "👾"

# Store the total number of aliens
total_aliens = 0

# Print the command saucer
spaces = " " * (formation_height * 2)
print(spaces + saucer)

print()

# Print alien rows
for row in range(1, formation_height + 1):

    spaces = " " * ((formation_height - row) * 2)

    fleet = (alien + " ") * row

    print(spaces + fleet)

    # Add the number of aliens in this row
    total_aliens = total_aliens + row

print()
print("Total aliens unleashed:", total_aliens)