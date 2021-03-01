# Genshin Impact Hoyolab Daily Reward collector

### How to use?

- Install python3 and (Optional)virtualenv
- (Optional)Create a virtual environment using `virtualenv -p python3 venv`
- (Optional)Activate virtualenv using `source venv/bin/activate` or `\env\Scripts\activate` on windows
- Run `pip install -r requirements.txt`
- (Optional)Install the relevant drivers using `webdrivermanager firefox chrome`
- Login to [hoyolab](https://hoyolab.com)
- Get relevant cookies mentioned in config.sample.py and put them in a new file named config.py
- Run the script as `py script.py` or `python3 script.py` (default chrome driver) or with the flags `-F/--firefox` for the firefox driver
