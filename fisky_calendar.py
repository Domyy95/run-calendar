import requests
from bs4 import BeautifulSoup
from google_calendar_api import create_event
from datetime import datetime
import re

# Put here the link of the fisky calendar
url = "https://www.skyrunningitalia.it/pages/Calendario-Gare-2024"


input_date_format = "%d/%m/%Y"
output_date_format = "%Y-%m-%d"


def convert_date(date: str) -> str:
    date_obj = datetime.strptime(date, input_date_format)
    date_str = date_obj.strftime(output_date_format)
    return date_str


pattern = re.compile(r"\s+")


def fix_str(str: str) -> str:
    str = re.sub(pattern, " ", str.strip())
    return str


response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find_all("tr")

    for row in rows:
        cells = row.find_all("td")

        if len(cells) >= 2:
            date = cells[0].text.strip()
            date = fix_str(date)

            event_name = cells[1].text.strip()
            location = cells[3].text.strip()

            km = cells[5].text.strip()
            km = fix_str(km)

            high_diff = cells[6].text.strip()
            high_diff = fix_str(high_diff)

            link_tag = cells[1].find("a")
            link = link_tag["href"] if link_tag and "href" in link_tag.attrs else "N/A"
            circuit = cells[4].text.strip()
            circuit = fix_str(circuit)

            print(
                f"""Date: {date}\nEvent Name: {event_name}\nlocation: {location}\nkm: {km}\nhigh_diff: {high_diff}\nlink: {link}\ncircuit: {circuit}"""
            )

            print(
                "\n0 - directly create the event\n1 - modify the date and create the event (if not in the format dd/mm/yyyy)\n2 - skip"
            )
            answer = input()

            if answer == "1":
                print("Insert the new date in the format dd/mm/yyyy")
                date = input()

            if answer in ["0", "1"]:
                desc = f"FISKY\n{link}\n{km}\n{high_diff}\n\n" + (
                    f"Circuito: {circuit}" if circuit != "" else ""
                )
                date_str = convert_date(date)
                date_obj = datetime.strptime(date, input_date_format)
                create_event(
                    title=event_name,
                    description=desc,
                    date=date_str,
                    location=location,
                )
                print("Event created")

else:
    print(f"Failed to fetch the content. Status code: {response.status_code}")
