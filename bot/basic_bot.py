import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        """Initialize the Basic Trading Bot for FUTURES"""
        self.logger = logging.getLogger(__name__)
        
        try:
            # CORRECT configuration for Futures Testnet
            self.client = Client(api_key, api_secret, testnet=testnet)
            
            # Set correct Futures URL for testnet
            if testnet:
                self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
            
            self.logger.info("Futures Bot initialized successfully")
            self._validate_connection()
        except Exception as e:
            self.logger.error(f"Failed to initialize bot: {e}")
            raise
    
    def _validate_connection(self):
        """Validate Futures API connection"""
        try:
            # Use futures_account() instead of get_account() for futures
            account_info = self.client.futures_account()
            self.logger.info("Futures API connection validated successfully")
            return True
        except BinanceAPIException as e:
            self.logger.error(f"Futures API validation failed: {e}")
            return False
    
    def get_account_balance(self):
        """Get Futures account balance information"""
        try:
            # Use futures_account_balance() for futures
            balances = self.client.futures_account_balance()
            # Filter balances with positive values
            positive_balances = [asset for asset in balances if float(asset['balance']) > 0]
            self.logger.info(f"Retrieved futures account balance for {len(positive_balances)} assets")
            return positive_balances
        except BinanceAPIException as e:
            self.logger.error(f"Failed to get futures account balance: {e}")
            return None
    
    def get_symbol_info(self, symbol):
        """Get symbol information for futures"""
        try:
            # Use futures_exchange_info() for futures
            info = self.client.futures_exchange_info()
            symbol_info = None
            for s in info['symbols']:
                if s['symbol'] == symbol:
                    symbol_info = s
                    break
            
            if symbol_info:
                self.logger.info(f"Retrieved futures symbol info for {symbol}")
            else:
                self.logger.warning(f"Symbol {symbol} not found in futures exchange info")
            
            return symbol_info
        except BinanceAPIException as e:
            self.logger.error(f"Failed to get futures symbol info for {symbol}: {e}")
            return None
    
    def place_market_order(self, symbol, side, quantity):
        """Place a market order on Futures"""
        try:
            # Use futures_create_order() for futures trading
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='MARKET',
                quantity=quantity
            )
            
            self.logger.info(f"Futures market {side} order placed: {order}")
            return order
            
        except BinanceAPIException as e:
            self.logger.error(f"Failed to place futures market order: {e}")
            return None
        except Exception as e:
            self.logger.error(f"Unexpected error placing futures market order: {e}")
            return None
    
    def place_limit_order(self, symbol, side, quantity, price):
        """Place a limit order on Futures"""
        try:
            # Use futures_create_order() for futures trading
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=str(price)
            )
            
            self.logger.info(f"Futures limit {side} order placed: {order}")
            return order
            
        except BinanceAPIException as e:
            self.logger.error(f"Failed to place futures limit order: {e}")
            return None
        except Exception as e:
            self.logger.error(f"Unexpected error placing futures limit order: {e}")
            return None
    
    def get_order_status(self, symbol, order_id):
        """Get Futures order status"""
        try:
            order = self.client.futures_get_order(symbol=symbol, orderId=order_id)
            self.logger.info(f"Retrieved futures order status for {order_id}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Failed to get futures order status: {e}")
            return None
    
    def cancel_order(self, symbol, order_id):
        """Cancel a Futures order"""
        try:
            result = self.client.futures_cancel_order(symbol=symbol, orderId=order_id)
            self.logger.info(f"Futures order {order_id} cancelled successfully")
            return result
        except BinanceAPIException as e:
            self.logger.error(f"Failed to cancel futures order: {e}")
            return None
