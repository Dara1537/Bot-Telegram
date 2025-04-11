from telegram.ext import Updater, CommandHandler
import requests

# Token Bot Telegram របស់អ្នក
BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

# អនុគមន៍ស្វាគមន៍
def start(update, context):
    update.message.reply_text(
        "សួស្តី! សូមប្រើបញ្ជា៖ /topup UID ចំនួន\nឧទាហរណ៍: /topup 123456789 100"
    )

# អនុគមន៍សម្រាប់ Topup
def topup(update, context):
    args = context.args
    if len(args) != 2:
        update.message.reply_text("សូមប្រើបែបនេះ៖ /topup UID ចំនួន")
        return

    uid, amount = args
    # អ្នកអាចប្ដូរ link API និង data ទៅសេវា provider របស់អ្នក
    try:
        response = requests.post("https://your-api-provider.com/topup", data={
            "uid": uid,
            "amount": amount
        })

        if response.status_code == 200:
            update.message.reply_text(f"Topup {amount} diamond ទៅ UID {uid} បានជោគជ័យ!")
        else:
            update.message.reply_text("បរាជ័យក្នុងការធ្វើ Topup។ សូមពិនិត្យម្តងទៀត។")
    except Exception as e:
        update.message.reply_text(f"កំហុសក្នុងការបញ្ជូន: {e}")

# ចាប់ផ្ដើម bot
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("topup", topup))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()