import logging
import requests
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

class WalletHistoryFetcher:
    """Class to fetch wallet transaction history using Moralis API."""

    def __init__(self, api_key: str):
        """Initialize wallet history fetcher.
        
        Args:
            api_key: Moralis API key
        """
        self.api_key = api_key
        self.base_url = "https://deep-index.moralis.io/api/v2.2/wallets/:address/history"
        self.headers = {
            "accept": "application/json",
            "X-API-Key": self.api_key
        }

    def get_wallet_history(
        self, 
        address: str, 
        chain: str = "eth", 
        limit: int = 100
    ) -> Optional[List[Dict]]:
        """Fetch transaction history for a given wallet address.
        
        Args:
            address: Wallet address to fetch history for
            chain: Blockchain to query (default: eth)
            limit: Maximum number of transactions to return (default: 100)
            
        Returns:
            List of transaction dictionaries or None if error occurs
        """
        try:
            url = f"{self.base_url}/{address}"
            params = {
                "chain": chain,
                "limit": limit
            }
            
            response = requests.get(
                url,
                headers=self.headers,
                params=params
            )
            response.raise_for_status()
            
            return response.json()
            
        except Exception as e:
            logger.error(f"Error fetching wallet history: {e}")
            return None

    def __str__(self) -> str:
        """Return string representation of the class."""
        return f"WalletHistoryFetcher(api_key={self.api_key})"