import logging
import os
import random
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# --- CONFIGURATION ---
# WARNING: Hardcoding secrets like the BOT_TOKEN is not recommended for security.
# It is safer to use environment variables in your hosting service (e.g., Render).
BOT_TOKEN = "8103941911:AAHg9ks7zZ2oDResrrwwjkUPEMpLVuds2A4"
ADMIN_USER_ID = "1726525830" # Kept for notifications
WEBSITE_LINK = "https://onlywin.ltd" # Changed to the website link


# --- CUSTOMIZABLE BOT CONTENT ---
CHANNEL_NAME = "OnlyWin"

WELCOME_MESSAGE = (
    "Hello {user_name}!\n\n"
    f"Welcome to **{CHANNEL_NAME}**, your key to unlocking guaranteed profits from sports betting through arbitrage.\n\n"
    "Confused? Don't be. Arbitrage betting is a mathematical strategy, not gambling. It's about exploiting price differences to ensure you **win every time**.\n\n"
    "👉 Type /askquery to see how it works and why you can't lose."
)

FEATURES_DESCRIPTION = (
    "**Our Service - Your Unfair Advantage:**\n\n"
    "✅ **Real-Time Alerts:** We find the arbitrage opportunities; you just place the bets. We do the hard work for you.\n"
    "✅ **Step-by-Step Guides:** We show you exactly how much to stake on each outcome to lock in your profit.\n"
    "✅ **Premium Tools:** Access our custom calculators and software that make arbitrage betting simple and fast.\n"
    "✅ **Dedicated Support:** Our team is here to guide you on your journey to consistent, risk-free returns.\n\n"
    f"Ready to start winning? Visit our website by typing /subscribe."
)

# Persuasive FAQs for the /askquery command
ARBITRAGE_FAQS = (
    "**Your Questions Answered - The Path to Guaranteed Profit**\n\n"
    "**(1) What is Arbitrage Betting?**\n"
    "It's a risk-free strategy. Different bookmakers have different odds on the same event. We identify when these odds create a situation where you can bet on all possible outcomes and be **guaranteed a profit**, no matter who wins. It's pure math, not luck.\n\n"
    "**(2) How can you guarantee a profit? Isn't that impossible?**\n"
    "It's not only possible; it's a market inefficiency. For example, Bookie A might have Team X to win at 2.10 odds, while Bookie B has Team Y to win at 2.10 odds. By betting the correct amount on both, you are mathematically guaranteed to make a profit. We find these opportunities for you 24/7.\n\n"
    "**(3) If it's risk-free, why isn't everyone doing it?**\n"
    "Because finding these opportunities (or 'arbs') is incredibly difficult and time-consuming. They can appear and disappear in minutes. You need sophisticated software and a dedicated team to find them consistently. **That's what we provide.**\n\n"
    "**(4) Is this legal?**\n"
    "Yes, it is 100% legal. You are simply placing bets on public websites. Bookmakers don't like it, but there is nothing illegal about being a smart investor.\n\n"
    "**Convinced? The only thing stopping you from making a profit is getting started.**\n"
    "👉 Click /subscribe to visit our site and join now!"
)


HELP_MESSAGE = (
    "**Welcome to the OnlyWin Assistant!**\n\n"
    "Our goal is to help you achieve consistent, risk-free profits through arbitrage betting.\n\n"
    "**Available Commands:**\n"
    "/start - Welcome message\n"
    "/subscribe - Visit our website to join\n"
    "/features - See what our service offers\n"
    "/askquery - Learn how arbitrage guarantees profit"
)


# --- SETUP LOGGING ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# --- BOT COMMAND HANDLERS ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.effective_user.first_name
    await update.message.reply_text(WELCOME_MESSAGE.format(user_name=user_name), parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(HELP_MESSAGE, parse_mode='Markdown')

async def features(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(FEATURES_DESCRIPTION, parse_mode='Markdown')

async def ask_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(ARBITRAGE_FAQS, parse_mode='Markdown')

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    subscribe_text = (
        "**Your journey to guaranteed profits starts now.**\n\n"
        "Click the link below to visit our official website and gain access to our exclusive tools and alerts.\n\n"
        f"➡️ **[Visit {CHANNEL_NAME}]({WEBSITE_LINK})**\n\n"
        "Stop gambling. Start investing."
    )
    await update.message.reply_text(subscribe_text, parse_mode='Markdown', disable_web_page_preview=True)

async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """A simple handler to guide users who type instead of using commands."""
    await update.message.reply_text(
        "I can help you understand how to make guaranteed profits. Please use one of the following commands:\n\n"
        "/features - To see what we offer.\n"
        "/askquery - To learn why our method is risk-free."
    )

# --- MAIN FUNCTION ---

def main() -> None:
    if not BOT_TOKEN:
        print("ERROR: Environment variable TELEGRAM_BOT_TOKEN must be set.")
        return

    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("subscribe", subscribe))
    application.add_handler(CommandHandler("features", features))
    application.add_handler(CommandHandler("askquery", ask_query))

    # Register a handler for any other text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))

    print(f"{CHANNEL_NAME} Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()

