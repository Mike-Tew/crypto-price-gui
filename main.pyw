# TODO
# Create labels after api call has been made
# Create a combo box for all crypto data
# Create labels for all cryptos


from tkinter import Tk, Frame, LabelFrame, Button, Label
from tkinter import ttk
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


class Crypto_Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Crypto Price GUI")
        self.geometry("+900+300")
        self.crypto_data = self.clean_crypto_data(self.get_crypto_data())
        self.crypto_select_box = ttk.Combobox(
            self, value=self.create_name_list(self.crypto_data)
        )
        self.crypto_select_box.grid(row=0, column=0, padx=20, pady=20)

        self.labels_frame = LabelFrame(self, text="Labels")
        self.labels_frame.grid(row=1, column=1)

    def get_crypto_data(self):
        """Call the coinmarketcap API and get current crypto information."""

        API_KEY = "baf0940b-64a8-4015-a41c-3e2df1009ad9"
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
        parameters = {"start": "1", "limit": "10", "convert": "USD"}
        headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": API_KEY}
        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            return json.loads(response.text)["data"]
            # print(json.dumps(crypto_info, indent=2))
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

    def clean_crypto_data(self, crypto_data):
        """Clean the crypto data by returning only the name, symbol, and price."""

        clean_data = []
        for crypto in crypto_data:
            info_dict = {}
            info_dict["name"] = crypto.get("name", "not found")
            info_dict["symbol"] = crypto.get("symbol", "not found")
            info_dict["price"] = crypto["quote"]["USD"].get("price", "not found")
            clean_data.append(info_dict)

        return clean_data

    def create_name_list(self, crypto_data):
        """Creating a list of only the crypto names."""

        crypto_name_list = []
        for crypto in crypto_data:
            crypto_name_list.append(crypto.get("name"))

        return crypto_name_list

    def create_crypto_label(self):
        pass


if __name__ == "__main__":
    crypto_gui = Crypto_Gui()
    crypto_gui.mainloop()