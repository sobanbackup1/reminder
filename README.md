# Reminder – Bark App

This is a Python script that sends notifications to your iOS device using the Bark app.

**Step 1**
Install the Bark app on your iOS device, open it, set it up, and copy the Bark URL provided in the app.

**Step 2**
Download the script to your Linux, Windows, or other device (Python 3 must be installed).

**Step 3**
Open the script and replace
`BARK_KEY = "yourkey"`
with your Bark key. The key should look like:
`https://api.day.app/yourkey/`

**Step 4**
Test the script by running:
`python3 yourfile.py`

**PS:**
This script can be used with `crontab -e` to send notifications at a specific time.
