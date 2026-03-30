import requests as request_api

class PhoneNumberValidator:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        print(api_key)
        self.api_url = "https://api.numlookupapi.com/v1/validate/"


    def validate(self, phone_number: str, country_code: str) -> bool:
        if not phone_number:
            raise ValueError("Phone number cannot be empty.")
        print(f'country_code={country_code}')
        
        response = self._make_api_request(phone_number, country_code)
        print(response)
        if response.ok:
            return response.json()["valid"]
        else:
            response.raise_for_status()

    def _make_api_request(self, phone_number: str, country_code: str) -> request_api.Response:
        headers = {"apikey": self.api_key}
        params = {}
        if country_code:
            params["country_code"] = country_code

        response = request_api.get(self.api_url + phone_number, params=params, headers=headers)
        print(response.request.body)
        print(response.request.headers)
        return response