import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# التوكن السري الخاص بالبوت
TOKEN = "9120185936:AAEmP2gT4dtYHhjvvHau..."  # ضع التوكن الصحيح الخاص بك هنا

# معرف القناة الرسمية
CHANNEL_ID = "@MedGrad26"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    first_name = user.first_name

    try:
        invite_link_obj = await context.bot.create_chat_invite_link(
            chat_id=CHANNEL_ID,
            name=f"السفير: {first_name} ({user_id})",
            creates_join_request=False
        )
        link = invite_link_obj.invite_link

        message = (
            f"أهلاً بك يا زميلنا العزيز **{first_name}** في شبكة سفراء التنسيقية العامة (دفعة 2026)! 🎓\n\n"
            f"🔗 **رابط الدعوة الخاص بك والمولد آلياً:**\n"
            f"`{link}`\n\n"
            f"📌 **طريقة العمل:**\n"
            f"• شارك هذا الرابط المخصص مع زملائك الخريجين.\n"
            f"• سيتم احتساب كل من ينضم عبر رابطك تلقائياً في إحصائيات القناة.\n"
            f"• عند وصولك إلى **100 خريج**، ستتم ترقيتك تلقائياً لصفة (**قائد مجموعة**)!"
        )
    except Exception as e:
        message = (
            f"أهلاً بك **{first_name}**!\n\n"
            f"يرجى التأكد من إضافة البوت كمشرف (Admin) في القناة الرسمية لتوليد رابطك التلقائي.\n"
            f"رابط القناة العامة: https://t.me/MedGrad26"
        )

    await update.message.reply_text(message, parse_mode="Markdown")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("البوت يعمل بنجاح...")
    app.run_polling()
