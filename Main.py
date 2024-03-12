from get_crypto_price import get_crypto_price
from currency_converter import CurrencyConverter
c = CurrencyConverter()
import time
from plyer import notification

#* Change the code as you wish

currency = 'USD' #* Change currency to convert if needed
crypto_currency = 'btc' #* Change crypto currency if needed ( coin name )

coin_value = c.convert(get_crypto_price(source = "bitstamp", crypto = crypto_currency, pair = "usd"), 'USD', currency); # No need to change this one

notification_title = 'Price update' #* Notification title String
def message(value):
    message = f'Bitcoin: {value}' #* Change notification display message
    return message
notification_icon_path = None  #* Path to the notification icon | None == No icon
notification_timeout = 20 #* Notification vanish time in seconds, Windows may be limiting this one if it's set on your computer ( default is 5 seconds )
loop_time = 10 #* Time to update and show notification in seconds

try:
    while True:
        coin_value = c.convert(get_crypto_price(source = "bitstamp", crypto = crypto_currency, pair = "usd"), 'USD', currency); #* Update value

        notification_message = message(coin_value) #* Update message

        notification.notify(
            title = notification_title,
            message = notification_message,
            app_icon = notification_icon_path,
            timeout = notification_timeout,
        )
        time.sleep(loop_time)
except KeyboardInterrupt: #* If you hit 'CTRL + C' on CMD, code will stop
    print("Script terminated.")