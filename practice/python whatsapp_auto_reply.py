# whatsapp_auto_reply.py
# Yeh script WhatsApp Web ke liye ek auto-reply bot banata hai jo specific trigger words par reply karta hai.
# Yeh Selenium ka use karta hai Chrome browser ko control karne ke liye.

import time  # Time-related functions ke liye
from selenium import webdriver  # Web browser automation ke liye
from selenium.webdriver.common.by import By  # Element location strategies ke liye
from selenium.webdriver.common.keys import Keys  # Keyboard keys simulate karne ke liye
from selenium.webdriver.support.ui import WebDriverWait  # Wait karne ke liye
from selenium.webdriver.support import expected_conditions as EC  # Expected conditions ke liye
from webdriver_manager.chrome import ChromeDriverManager  # ChromeDriver automatically manage karne ke liye

# Reply text jo bot bhejega
REPLY_TEXT = "Hle kahiye! Kaise ho aap? Main ek chhota AI-style auto-reply bot hoon 😊"

def start_driver():
    # Chrome options set karte hain
    options = webdriver.ChromeOptions()
    # Session preserve karne ke liye user data dir set karte hain, taaki har baar QR scan na karna pade
    options.add_argument(r"--user-data-dir=./chrome_whatsapp_profile")
    # ChromeDriver automatically install aur use karte hain
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()  # Window maximize karte hain
    return driver





    

def wait_for_whatsapp_ready(driver, timeout=60):
    # WhatsApp Web open karte hain
    driver.get("https://web.whatsapp.com")
    print("Open WhatsApp Web — login if needed. Waiting for chats to load...")
    # Search box ka wait karte hain jo batata hai ki WhatsApp load ho gaya
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="chat-list-search"]'))
        )
        print("WhatsApp Web ready.")
        return True
    except Exception:
        raise RuntimeError("WhatsApp Web did not load in time. Make sure to scan QR and allow it to load.")

def get_all_chats(driver):
    # Left panel mein sab chats ke elements laate hain
    chats = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="cell-frame-container"]')
    return chats

def open_chat(chat):
    # Chat click karke open karte hain
    chat.click()
    time.sleep(1)  # Thoda wait karte hain taaki load ho jaye

def get_last_message_text(driver):
    # Current chat mein last incoming message ka text laate hain
    try:
        # Sab incoming messages dhundhte hain
        msgs = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="msg-container"] div.message-in span.selectable-text')
        if not msgs:
            return ""
        # Last message ka text
        last = msgs[-1].text
        return last.strip()
    except Exception:
        return ""

def send_message_in_chat(driver, text):
    # Message input box mein text type karke send karte hain
    try:
        inputbox = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="compose-input"]')
    except:
        # Fallback
        try:
            inputbox = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@spellcheck='true']")
        except:
            print("Input box not found.")
            return
    inputbox.click()
    inputbox.send_keys(text + Keys.ENTER)

def main_loop():
    driver = start_driver()
    try:
        wait_for_whatsapp_ready(driver, timeout=120)
        replied = set()  # Track karte hain kis chat ko reply kiya
        while True:
            chats = get_all_chats(driver)
            # Pehle 10 chats check karte hain
            for chat in chats[:10]:
                try:
                    # Chat ka title laate hain
                    title_el = chat.find_element(By.CSS_SELECTOR, 'span[data-testid="cell-frame-title"]')
                    chat_title = title_el.text
                except Exception:
                    chat_title = "unknown"

                open_chat(chat)
                time.sleep(0.8)  # Messages load hone ka wait
                last_text = get_last_message_text(driver).lower()
                print(f"[{chat_title}] last: {last_text}")

                trigger_words = ["hello", "helo", "hi", "hlo"]
                if any(w in last_text for w in trigger_words):
                    # Agar pehle reply nahi kiya to reply karte hain
                    if chat_title not in replied:
                        send_message_in_chat(driver, REPLY_TEXT)
                        print(f"Replied to {chat_title}")
                        replied.add(chat_title)
                else:
                    # Agar trigger nahi mila to replied se remove karte hain taaki future mein reply kar sake
                    if chat_title in replied:
                        replied.remove(chat_title)
                time.sleep(0.5)
            # Next scan ke liye wait
            time.sleep(3)
    except KeyboardInterrupt:
        print("Stopping.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main_loop()
