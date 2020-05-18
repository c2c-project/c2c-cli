# Quickstart

## The .env file

Use valid credentials from your `.env` file

1. RESPONSE_KEY - obtained from initial logmein api setup
2. CONSUMER_KEY - obtained from initial logmein api setup
3. CONSUMER_SECRET - obtained from initial logmein api setup
4. ACCESS_TOKEN - obtained from querying appropriate logmein api route
5. REFRESH_TOKEN - obtained when querying for access_token
6. ORGANIZER_KEY - related to your account
7. ACCOUNT_KEY - related to your account
8. WEBINAR_KEY - specific webinar you would like to perform actions on

## Obtaining an access token & refresh token
FYI, the previous `refresh_token` is used to obtain the next `(access_token, refresh_token)` pair, so you must already have a valid `refresh_token` inside of your `.env` file

```bash
python3 logmein.py --refresh
```

The terminal will display the new `access_token` and `refresh_token` -- copy and paste those into your .env file before running anything else. In the future, this will be automatically done. The access token is valid for 1 hour.

# The CSV file

Must have the following headers:

1. "email"
2. "firstName"
3. "lastName"

**NOTE:** case matters

## Using the CLI

Run the command

```bash
python3 logmein.py --csv <path to csv file of participants>
```

All participants will be uploaded at a rate of 1 per second.
