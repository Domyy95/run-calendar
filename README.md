# Write Fisky Calendar Events to your running Google Calendar 

## Description
This Python script scrapes event details from the Fisky calendar website and allows the user to add selected events to their Google Calendar.

## requirements
- Python 3
- install requirements with `pip install -r requirements.txt`
- Google Calendar API credentials 

### Google Calendar API Credentials

1. Go to the Google Cloud Console.
2. Create a new project or select an existing one.
3. Enable the "Google Calendar API" for your project.
4. Create Service Account Credentials:
    - In the Cloud Console, navigate to the "APIs & Services" > "Credentials" section.
    - Click on "Create credentials" and select "Service account key."
    - Choose or create a service account, set the role to "Project" > "Editor" (or another appropriate role), and select JSON as the key type.
Click "Create" to download the JSON key file.
Share Google Calendar with Service Account Email:

Open your Google Calendar.
Share your calendar with the email address associated with the service account (found in the JSON key file).

## Features
- Utilizes requests and BeautifulSoup for web scraping.
- Parses event details such as date, event name, location, distance, elevation, link, and circuit from the Fisky calendar.
- Interactively prompts the user to add events to their Google Calendar.
- Integrates with the Google Calendar API to create events.

## Usage
1. Set the Fisky calendar URL in the 'url' variable.
2. Run the script to fetch and display upcoming events.
3. Choose whether to add each event to your Google Calendar.

