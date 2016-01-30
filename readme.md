# lunchable

**lunchable** is a Python application to send [feinessen][fe]'s daily lunch menu as a text message using the Twilio API.

## Installation

1. Clone this repo and `cd` in.
2. `$ virtualenv env`
3. `$ source env/bin/activate`
4. `$ pip install -r requirements.txt`

## Usage

1. Create a Twilio account and get your twilio number, account and token keys.
2. Enter the corresponding number, tokens, and however many recipients you want in `config.py`.  
    *Note: using Twilio in trial mode needs you to verify recipient's numbers first.*  
    *Note: if you add or remove recipients do not forget to change `scraping.py` accordingly.*
3. Create a free Heroku app and set it up accordingly (dyno type `web`, size `0`.)
4. Push `lunchable` to Heroku.
5. Create a new Heroku Scheduler add-on instance;  
    set the shell command to `python scraping.py`, dyno size to “free,” frequency to “daily,” and select a UTC time relevant to your timezone (for instance, if you're in CET, 10AM UTC is fine.)

## License

MIT

[fe]: http://feinessen.at
