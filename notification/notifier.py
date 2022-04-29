from requests import request

TELEGRAM_CHAT_ID = "1105104825"
TELEGRAM_BOT_TOKEN = "5125202288:AAGUfRZ2WEXIk4sjmldP17PI48yKnhIZX28"

def send_tg_notif(filename, filepath, filemime, domain) -> bool:
    bot_token = TELEGRAM_BOT_TOKEN

    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "caption": "Scan complete for " + domain + ". File attached."}

    files = [
        (
            "document",
              (
                  filename,
                  open(filepath, "rb"),
                  filemime,
              )
        )
    ]

    response = request("POST", url, data=payload, files=files)
    if response.status_code == 200:
        return True
    print(response.status_code)
    return False

def send_reports_to_tg(domain):
    send_tg_notif("arjun.json", r"C:\Programming\ISM\Easy Scan\temp_db\arjun.json", "application/json", domain)
    send_tg_notif("probe.txt", r"C:\Programming\ISM\Easy Scan\temp_db\probe.txt", "plain/text", domain)
    send_tg_notif("subdomains.txt", r"C:\Programming\ISM\Easy Scan\temp_db\subdomains.txt", "plain/text", domain)
