from tkinter import *
import requests
import json
from  tkinter import messagebox as mb
from tkinter import ttk


def update_currency_label(event):
    code = currency_combobox.get()
    name = curr[code]
    currency_label.config(text=name)


def update_crypto_label(event):
    code = crypto_combobox.get()
    name = crypta[code]
    crypto_label.config(text=name)

def exchange():
    crypto_code = crypto_combobox.get()
    currency_code = currency_combobox.get()
    crypto_code_result = crypto_code.lower()
    currency_code_result = currency_code.lower()
    exch_rate = 0
    if crypto_code and currency_code:
        try:
            headers = {'accept': 'application/json'}
            response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_code_result}&vs_currencies={currency_code_result}", headers=headers)
            response.raise_for_status()
            #data = response.json()
            data = json.loads(response.text)
            price = data[crypto_code.lower()][currency_code.lower()]
            if crypto_code_result in data:
                exch_rate = data[crypto_code_result][currency_code_result]
                crypto_name = crypta[crypto_code]
                currency_name = curr[currency_code]
                exch_label.config(text=f"Курс обмена:\n {exch_rate:.2f} {currency_name}\n за один {crypto_name}")
                #mb.showinfo("Курс обмена", f"Курс: {exchange_rate1:.2f} {target_name} за один {base_name1}")
            else:
                exch_label.config(text=f"Ошибка! Валюта {crypto_code} не найдена!")
                #mb.showerror("Ошибка!", f"Валюта {target_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}!")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")


curr = {
    "RUB": "Российский рубль",
    "USD": "Доллар США",
    "GBP": "Британский фунт стерлингов",
    "AED": "Дирхам ОАЭ",
    "AFN": "Афгани",
    "ALL": "Албанский лек",
    "AMD": "Армянский драм",
    "ANG": "Нидерландский антильский гульден",
    "AOA": "Ангольская кванза",
    "ARS": "Аргентинское песо",
    "AUD": "Австралийский доллар",
    "AWG": "Арубанский флорин",
    "AZN": "Азербайджанский манат",
    "BAM": "Конвертируемая марка Боснии и Герцеговины",
    "BBD": "Барбадосский доллар",
    "BDT": "Бангладешская така",
    "BGN": "Болгарский лев",
    "BHD": "Бахрейнский динар",
    "BIF": "Бурундийский франк",
    "BMD": "Бермудский доллар",
    "BND": "Брунейский доллар",
    "BOB": "Боливийский боливиано",
    "BRL": "Бразильский реал",
    "BSD": "Багамский доллар",
    "BTN": "Бутанский нгултрум",
    "BWP": "Ботсванская пула",
    "BYN": "Белорусский рубль",
    "BZD": "Белизский доллар",
    "CAD": "Канадский доллар",
    "CDF": "Конголезский франк",
    "CHF": "Швейцарский франк",
    "CLP": "Чилийское песо",
    "CNY": "Китайский юань",
    "COP": "Колумбийское песо",
    "CRC": "Костариканский колон",
    "CUP": "Кубинское песо",
    "CVE": "Эскудо Кабо-Верде",
    "CZK": "Чешская крона",
    "DJF": "Франк Джибути",
    "DKK": "Датская крона",
    "DOP": "Доминиканское песо",
    "DZD": "Алжирский динар",
    "EGP": "Египетский фунт",
    "ERN": "Эритрейская накфа",
    "ETB": "Эфиопский быр",
    "EUR": "Евро",
    "FJD": "Доллар Фиджи",
    "FKP": "Фунт Фолклендских островов",
    "FOK": "Фарерская крона",
    "GEL": "Грузинский лари",
    "GGP": "Фунт Гернси",
    "GHS": "Ганский седи",
    "GIP": "Гибралтарский фунт",
    "GMD": "Гамбийский даласи",
    "GNF": "Гвинейский франк",
    "GTQ": "Гватемальский кетсаль",
    "GYD": "Гайанский доллар",
    "HKD": "Гонконгский доллар",
    "HNL": "Гондурасская лемпира",
    "HRK": "Хорватская куна",
    "HTG": "Гаитянский гурд",
    "HUF": "Венгерский форинт",
    "IDR": "Индонезийская рупия",
    "ILS": "Израильский шекель",
    "IMP": "Фунт Острова Мэн",
    "INR": "Индийская рупия",
    "IQD": "Иракский динар",
    "IRR": "Иранский риал",
    "ISK": "Исландская крона",
    "JEP": "Фунт Джерси",
    "JMD": "Ямайский доллар",
    "JOD": "Иорданский динар",
    "JPY": "Японская иена",
    "KES": "Кенийский шиллинг",
    "KGS": "Киргизский сом",
    "KHR": "Камбоджийский риель",
    "KID": "Доллар Кирибати",
    "KMF": "Франк Комор",
    "KRW": "Южнокорейская вона",
    "KWD": "Кувейтский динар",
    "KYD": "Доллар Каймановых островов",
    "KZT": "Казахстанский тенге",
    "LAK": "Лаосский кип",
    "LBP": "Ливанский фунт",
    "LKR": "Шри-ланкийская рупия",
    "LRD": "Либерийский доллар",
    "LSL": "Лоти Лесото",
    "LYD": "Ливийский динар",
    "MAD": "Марокканский дирхам",
    "MDL": "Молдавский лей",
    "MGA": "Малагасийский ариари",
    "MKD": "Северомакедонский динар",
    "MMK": "Мьянманский кьят",
    "MNT": "Монгольский тугрик",
    "MOP": "Патака Макао",
    "MRU": "Мавританская угия",
    "MUR": "Маврикийская рупия",
    "MVR": "Мальдивская руфия",
    "MWK": "Малавийская квача",
    "MXN": "Мексиканское песо",
    "MYR": "Малайзийский ринггит",
    "MZN": "Мозамбикский метикал",
    "NAD": "Намибийский доллар",
    "NGN": "Нигерийская найра",
    "NIO": "Никарагуанская кордоба",
    "NOK": "Норвежская крона",
    "NPR": "Непальская рупия",
    "NZD": "Новозеландский доллар",
    "OMR": "Оманский риал",
    "PAB": "Панамский бальбоа",
    "PEN": "Перуанский соль",
    "PGK": "Кина Папуа-Новой Гвинеи",
    "PHP": "Филиппинское песо",
    "PKR": "Пакистанская рупия",
    "PLN": "Польский злотый",
    "PYG": "Парагвайский гуарани",
    "QAR": "Катарский риал",
    "RON": "Румынский лей",
    "RSD": "Сербский динар",
    "RWF": "Франк Руанды",
    "SAR": "Саудовский риал",
    "SBD": "Доллар Соломоновых островов",
    "SCR": "Сейшельская рупия",
    "SDG": "Суданский фунт",
    "SEK": "Шведская крона",
    "SGD": "Сингапурский доллар",
    "SHP": "Фунт Святой Елены",
    "SLE": "Леоне Сьерра-Леоне",
    "SLL": "Сьерра-леонский леоне",
    "SOS": "Сомалийский шиллинг",
    "SRD": "Суринамский доллар",
    "SSP": "Южносуданский фунт",
    "STN": "Добра Сан-Томе и Принсипи",
    "SYP": "Сирийский фунт",
    "SZL": "Свазилендский лилангени",
    "THB": "Тайский бат",
    "TJS": "Таджикский сомони",
    "TMT": "Туркменский манат",
    "TND": "Тунисский динар",
    "TOP": "Паанга Тонга",
    "TRY": "Турецкая лира",
    "TTD": "Доллар Тринидада и Тобаго",
    "TVD": "Доллар Тувалу",
    "TWD": "Тайваньский доллар",
    "TZS": "Танзанийский шиллинг",
    "UAH": "Украинская гривна",
    "UGX": "Угандийский шиллинг",
    "UYU": "Уругвайское песо",
    "UZS": "Узбекский сум",
    "VES": "Венесуэльский боливар",
    "VND": "Вьетнамский донг",
    "VUV": "Вату Вануату",
    "WST": "Тала Самоа",
    "XAF": "Франк КФА BEAC",
    "XCD": "Восточно-карибский доллар",
    "XDR": "СПЗ (Специальные права заимствования)",
    "XOF": "Франк КФА BCEAO",
    "XPF": "Французский тихоокеанский франк",
    "YER": "Йеменский риал",
    "ZAR": "Южноафриканский рэнд",
    "ZMW": "Замбийская квача",
    "ZWL": "Зимбабвийский доллар"
}

crypta = {
    "Bitcoin": "Биткоин",
    "Litecoin": "Лайткоин",
    "Ethereum": "Эфириум",
    "Ethereum-Classic": "Эфириум классический",
    "Ripple": "XRP",
    "Cardano": "ADA"
}

window = Tk()
window.title("Курсы обмена криптовалюты")
window.geometry("360x450")

label1 = (Label(text="Валюта"))
label1.pack(padx=10, pady=10)
currency_combobox = ttk.Combobox(values=list(curr.keys()))
currency_combobox.pack(padx=10, pady=10)
currency_combobox.bind("<<ComboboxSelected>>", update_currency_label)
currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Label(text="Криптовалюта").pack(padx=10, pady=10)

crypto_combobox = ttk.Combobox(values=list(crypta.keys()))
crypto_combobox.pack(padx=10, pady=10)
crypto_combobox.bind("<<ComboboxSelected>>", update_crypto_label)

crypto_label = ttk.Label()
crypto_label.pack(padx=10, pady=10)

exch_label = ttk.Label()
exch_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
