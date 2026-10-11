# command = ["move", "north"]
command = ["attack", "npc"]

match command:
    case ["move", direction]:
        print(f"Moving {direction}")
    case ["attack", object]:
        print(f"Attacking {object}")


if command[0] == "move":
    print(f"Moving {command[1]}")
elif command[0] == "attack":
    print(f"Attacking {command[1]}")
