from google_calendar_api import create_event

year = "2024"

while True:
    print("Insert the date in the format MM-DD")
    date = input()
    date = f"{year}-{date}"
    print("Insert the event name")
    event_name = input()
    print("Insert the location")
    location = input()
    print("Insert the link")
    link = input()
    print("Insert the circuit")
    circuit = input()
    print("Insert the km")
    km = input()
    km = f"Km {km}"
    print("Insert the high_diff")
    high_diff = input()
    high_diff = f"D+ {high_diff}"

    desc = (
        (f"{link}\n" if link != "" else "")
        + f"{km}\n{high_diff}\n\n"
        + (f"Circuito: {circuit}" if circuit != "" else "")
    )

    create_event(
        title=event_name,
        description=desc,
        date=date,
        location=location,
    )

    print("Do you want to create another event? (y/n)")
    answer = input()
    if answer == "n":
        break
