# Discord Status Changer

A streamlined Python tool for automated Discord custom status rotation via API.

---

## Configuration

### config.json
```json
{
  "token": "YOUR_ACCOUNT_TOKEN",
  "clear_enabled": false,
  "clear_interval": 60,
  "sleep_interval": 10,
  "random": true
}
```
---

## Configuration

* **token**: Discord account authorization token.
* **clear_enabled**: Toggle for periodic console clearing.
* **clear_interval**: Amount of status changes before the console clears.
* **sleep_interval**: Delay in seconds between updates.
* **random**: Enables random status selection and dynamic timing.

### statuses.txt
Add your desired statuses to this file, **one per line**. The script will automatically read them on startup.

---

## Usage

1. **Install the required library**:
   `pip install requests`
2. **Setup**:
   Ensure `config.json` and `statuses.txt` are in the same folder as the script.
3. **Run**:
   `python main.py`

---

## Disclaimer
Automating user accounts (self-bots) violates **Discord's Terms of Service**. Use at your own risk.
