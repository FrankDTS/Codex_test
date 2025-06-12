# Codex_test

This repository contains a minimal example demonstrating how you might combine Google Calendar and Asana tasks into a simple web dashboard.

## Setup

1. Install dependencies (create a virtual environment if desired):

```bash
pip install Flask google-api-python-client asana
```

2. Obtain credentials:
   - Create a Google Cloud project and enable the Calendar API. Download OAuth credentials.
   - Generate an Asana personal access token from your Asana account settings.
   - Store these credentials in environment variables or a configuration file.

3. Run the example application:

```bash
python integration/app.py
```

The app will fetch example data from Google Calendar and Asana (the current code uses static placeholders). Browse to `http://localhost:5000/` to view a simple timeline and status dashboard. The raw merged data is available at `http://localhost:5000/api/data`.

## Next Steps

- Replace the placeholder functions in `integration/app.py` with real API calls.
- Add authentication and replace the placeholder APIs with real calls.
- Customize the HTML templates for your preferred style and add additional features.
