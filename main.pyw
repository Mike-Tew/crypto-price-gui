from tkinter import Tk, Frame, Button, Label
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


class Crypto_Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Crypto Price GUI")
        self.geometry("+900+300")

        self.info_button = Button(self, text="Get Info", command=self.get_crypto_data)
        self.info_button.grid(row=0, column=0)

    def get_crypto_data(self):
        """Call the coinmarketcap API and get current crypto information."""

        API_KEY = "baf0940b-64a8-4015-a41c-3e2df1009ad9"
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
        parameters = {
            "start": "1",
            "limit": "10",
            "convert": "USD"
        }
        headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": API_KEY}
        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            crypto_info = json.loads(response.text)["data"]
            print(json.dumps(crypto_info, indent=2))
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

    def create_crypto_label(self):
        pass


if __name__ == "__main__":
    crypto_gui = Crypto_Gui()
    crypto_gui.mainloop()