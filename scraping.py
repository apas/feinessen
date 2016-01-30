import requests, json, datetime, locale, config
from lxml import html
from twilio.rest import TwilioRestClient

try:
  locale.setlocale(locale.LC_TIME, "de_DE.utf8") # heroku locale
except Exception:
  locale.setlocale(locale.LC_TIME, "de_DE") # local locale

account = config.twilio_account
token = config.twilio_token
client = TwilioRestClient(account, token)

page = requests.get("http://www.feinessen.at/")
tree = html.fromstring(page.content)

monday = tree.xpath("//span[@style='color:#000000;']/text()")
meals = tree.xpath("//span[@style='color: rgb(0, 0, 0); font-family: Helvetica; text-align: start;']/text()")
days = tree.xpath("//span[@style='color: rgb(0, 0, 0);']/text()")

# remove duplicates
for index, meal in enumerate(meals):
  current = meal.split(" ")
  current = current[0]
  try:
    next = meals[index + 1]
  except Exception as e:
    print "end of list"
    break
  if current in next:
    meals.pop(index)

meals[5:] = [] # get only first 5 items
days.insert(0, monday[0]) # insert monday as first elem in list
today = datetime.datetime.now()

food_dict = {}
for i in range(0,5):
  food_dict[days[i]] = meals[i]

menu = ""
for i in food_dict:
  t = i.split(",")
  if t[0].capitalize() == today.strftime("%A"):
    menu = i + ":\n" + food_dict[i]
    print menu.encode("utf-8")
  else:
    pass

if today.isoweekday() in range(1, 6):
  message = client.messages.create(to=config.recipient1, from_=config.from_twilio,
    body=menu)
  message = client.messages.create(to=config.recipient2, from_=config.from_twilio,
    body=menu)
  message = client.messages.create(to=config.recipient3, from_=config.from_twilio,
    body=menu) 
