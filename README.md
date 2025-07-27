# 🚀 Binance Futures Trading Bot

A professional-grade Python-based command-line trading bot for Binance USDT-M Futures. It supports **market and limit orders**, comes with **modular architecture**, **robust logging**, and **error handling** ideal for showcasing your backend engineering and trading automation skills.

---

## 📈 Live Test Summary

✅ **Recent Order Executions**
- Market BUY (BTCUSDT - 0.001 BTC) → Order ID: `5482457927`
- Limit SELL (BTCUSDT - 0.002 BTC @ $65,000) → Order ID: `5482489500`
- Market BUY (BTCUSDT - 0.002 BTC) → Order ID: `5482492671`
- Market SELL (ETHUSDT - 0.05 ETH) → Order ID: `4933331259`

---

## 🔥 Features

### ✅ Trading Logic
- Market Orders (BTCUSDT, ETHUSDT)
- Limit Orders with price validation
- Quantity checks for Binance notional limits
- Testnet execution to simulate real trades safely

### ✅ Technical Stack
- CLI with `argparse`
- Modular architecture
- Logging with timestamps and severity
- Secure `.env`-based API key management
- Error handling for API/network exceptions

---

## 🏗️ Project Structure

```
binance_trading_bot/
├── bot/
│   ├── __init__.py                 # Package initialization
│   └── basic_bot.py                # Order placement logic
├── config/
│   ├── __init__.py                 # Package initialization
│   └── logging_config.py           # Custom logger setup
├── logs/                           # Generated logs with timestamps
│   └── bot_*.log
├── .env.example                    # Environment variable template for API keys
├── .gitignore                      # Ignore sensitive and unnecessary files
├── main.py                         # CLI entry point and argument parser
├── README.md                       # Project documentation
└── requirements.txt                # Python package dependencies
```

---

## ⚙️ Installation & Setup

### ✅ Prerequisites
- Python 3.8+
- Binance Testnet account
- Virtual environment (`venv`)

### 💡 Steps

```bash
# 1. Clone repository
git clone https://github.com/your-username/binance-futures-trading-bot.git
cd binance-futures-trading-bot

# 2. Create virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add Binance API keys
cp .env.example .env
# Edit .env with your testnet keys from https://testnet.binancefuture.com/
```

---

## 🛠️ Usage Examples

### ✅ Market Orders

```bash
# Buy BTC
python main.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001

# Sell ETH
python main.py --symbol ETHUSDT --side SELL --order-type MARKET --quantity 0.05
```

### ✅ Limit Orders

```bash
# Buy BTC @ $45,000
python main.py --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.002 --price 45000

# Sell ETH @ $4,000
python main.py --symbol ETHUSDT --side SELL --order-type LIMIT --quantity 0.1 --price 4000
```

---

## 🔍 Sample Output

```bash
$ python main.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001

2025-07-27 15:01:24 - config.logging_config - INFO - Logging initialized.
2025-07-27 15:01:25 - bot.basic_bot - INFO - Bot connected to Binance Testnet

Placing MARKET BUY order...
✅ Order placed successfully!
Order ID: 5482457927
Status: NEW
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001
```

📸 Screenshots of order execution:
![screenshot1](https://github.com/user-attachments/assets/0bba4619-6cd7-44a0-b1c2-b8e15df32824)
![screenshot2](https://github.com/user-attachments/assets/bde7c16b-9c55-4d4b-9248-90b55fb04268)
![screenshot3](https://github.com/user-attachments/assets/df0fce8e-8682-4ff2-b396-fc24c325f1fa)

---

## 🔐 Environment Variables

`.env.example`:
```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret
TESTNET=True

LOG_LEVEL=INFO
LOG_FILE=logs/bot.log
```

---

## 🧾 Logging System

- Timestamped logs for all actions
- API responses saved
- Order confirmations
- Errors with stack traces

📂 Log files:
```
logs/
├── bot_20250727_150124.log
├── bot_20250727_152155.log
└── bot_20250727_153244.log
```

📝 Example log entry:
```log
2025-07-27 15:21:56 - bot.basic_bot - INFO - Futures market BUY order placed: {
  'orderId': 5482457927,
  'symbol': 'BTCUSDT',
  'status': 'NEW',
  'side': 'BUY',
  'type': 'MARKET',
  'quantity': '0.001'
}
```

---

## 🧪 Testing Scenarios

✅ Covered test cases:
- Valid market and limit orders for BTC and ETH
- Invalid quantity below minimum notional
- Invalid limit price (too far from market)
- Missing CLI arguments
- Invalid trading symbol
- Network error fallback with retry

---

## 🚨 Troubleshooting

### ❗ Error: "Order's notional must be no smaller than 100"
💡 Increase quantity or choose a cheaper asset

### ❗ Error: "LIMIT price too far from market"
💡 Price must be within ±10% of current market price

### ❗ API Errors or "Invalid API key"
💡 Verify `.env` keys or switch between testnet/mainnet

---

## 📦 Dependencies

```txt
python-binance==1.0.19
python-dotenv==1.0.0
```

---

## 🤝 Contributing

```bash
# Fork, branch, and push your changes
git checkout -b feature/your-feature
git commit -m "Add new feature"
git push origin feature/your-feature
```

Then open a Pull Request 🚀

---

## 📜 License

This project is licensed under the **MIT License** – see `LICENSE` file for details.

---

## 🏆 Achievements

✅ Executed real testnet trades  
✅ CLI-driven design  
✅ Logs everything to disk  
✅ API-secured with .env  
✅ Industry-aligned project structure

---

## 📬 Contact

**Developer**: Jayesh Kamble  
**LinkedIn**: [Jayesh Kamble](https://www.linkedin.com/in/jayesh-kamble-/)

---


⭐ **If this project helped you, give it a star!**  
*Built with 💻 and 💡 to learn algorithmic trading and backend Python systems.*
