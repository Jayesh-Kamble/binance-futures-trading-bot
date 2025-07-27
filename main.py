#!/usr/bin/env python3
"""
Binance Futures Trading Bot
A simple command-line trading bot for Binance Futures Testnet
"""

import argparse
import os
import sys
from dotenv import load_dotenv
from bot.basic_bot import BasicBot
from config.logging_config import setup_logging

def validate_inputs(args):
    """Validate user inputs"""
    errors = []
    
    if not args.symbol:
        errors.append("Symbol is required")
    
    if not args.side or args.side.upper() not in ['BUY', 'SELL']:
        errors.append("Side must be BUY or SELL")
    
    if not args.quantity or float(args.quantity) <= 0:
        errors.append("Quantity must be positive")
    
    if args.order_type.upper() == 'LIMIT' and (not args.price or float(args.price) <= 0):
        errors.append("Price is required for limit orders")
    
    return errors

def main():
    # Setup logging
    setup_logging()
    
    # Load environment variables
    load_dotenv()
    
    parser = argparse.ArgumentParser(description='Binance Futures Trading Bot')
    parser.add_argument('--symbol', required=True, help='Trading symbol (e.g., BTCUSDT)')
    parser.add_argument('--side', required=True, choices=['BUY', 'SELL'], help='Order side')
    parser.add_argument('--order-type', required=True, choices=['MARKET', 'LIMIT'], help='Order type')
    parser.add_argument('--quantity', required=True, type=float, help='Order quantity')
    parser.add_argument('--price', type=float, help='Order price (required for limit orders)')
    parser.add_argument('--test', action='store_true', help='Use test orders')
    args = parser.parse_args()
    # Validate inputs
    errors = validate_inputs(args)
    if errors:
        print("Input validation errors:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    
    # Get API credentials
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    testnet = os.getenv('TESTNET', 'True').lower() == 'true'
    
    if not api_key or not api_secret:
        print("Error: BINANCE_API_KEY and BINANCE_API_SECRET must be set in .env file")
        sys.exit(1)
    
    try:
        # Initialize bot
        print(f"Initializing bot with testnet={testnet}")
        bot = BasicBot(api_key, api_secret, testnet=testnet)
        
        # Show account balance - CORRECTED FOR FUTURES
        print("\nAccount Balance:")
        balances = bot.get_account_balance()
        if balances:
            for balance in balances[:5]:  # Show first 5 assets
                # FIXED: Use 'balance' instead of 'free' for futures
                print(f"  {balance['asset']}: {balance['balance']}")
        else:
            print("  No balances found or error retrieving balances")
        
        # Get symbol info
        print(f"\nSymbol Info for {args.symbol}:")
        symbol_info = bot.get_symbol_info(args.symbol)
        if symbol_info:
            print(f"  Status: {symbol_info['status']}")
            print(f"  Base Asset: {symbol_info['baseAsset']}")
            print(f"  Quote Asset: {symbol_info['quoteAsset']}")
        else:
            print("  Could not retrieve symbol info")
        
        # Place order
        print(f"\nPlacing {args.order_type} {args.side} order...")
        print(f"Symbol: {args.symbol}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price: {args.price}")
        
        if args.order_type.upper() == 'MARKET':
            order = bot.place_market_order(args.symbol, args.side, args.quantity)
        else:
            order = bot.place_limit_order(args.symbol, args.side, args.quantity, args.price)
        
        if order:
            print("\n🎉 Order placed successfully!")
            print(f"Order ID: {order.get('orderId')}")
            print(f"Status: {order.get('status')}")
            print(f"Symbol: {order.get('symbol')}")
            print(f"Side: {order.get('side')}")
            print(f"Type: {order.get('type')}")
            print(f"Quantity: {order.get('origQty')}")
            if 'price' in order:
                print(f"Price: {order.get('price')}")
        else:
            print("❌ Failed to place order. Check logs for details.")
            sys.exit(1)
    
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
