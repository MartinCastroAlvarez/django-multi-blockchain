"""
Business Logic related to this specific blockchain network.
"""

import requests
from django.conf import settings


class AccountLogic:
    """
    Wraper for blockchain accounts logic.
    """

    @staticmethod
    def get_balance(wallet: str) -> int:
        """
        Returns the balance for a given wallet
        """
        params: dict = {'chain': settings.MORALIS_CHAIN_ID}
        url: str = f'{settings.MORALIS_SERVER_URL}/{wallet}/balance'
        headers: dict = {'X-Api-Key': settings.MORALIS_MASTER_KEY}
        response: requests.Response = requests.get(url, headers=headers, params=params)
        return response.json()['balance']
