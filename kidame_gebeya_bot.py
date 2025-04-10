import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "MY_API"
bot = telebot.TeleBot(TOKEN)

PRODUCTS = {
    "M001": {"name": "iPad", "price": 68000, "photo": "C002.jpg", "category": "Mobile", "stock": 5, "description": "Apple iPad with Retina display."},
    "M002": {"name": "ZET Mobile", "price": 17000, "photo": "C003.jpg", "category": "Mobile", "stock": 10, "description": "Affordable smartphone with great battery life."},
    "M009": {"name": "Fast Charger", "price": 1550, "photo": "C005.jpg", "category": "Accessories", "stock": 20, "description": "Super fast charger for all mobile devices."},

    "C001": {"name": "Computer", "price": 37010, "photo": "C002.jpg", "category": "Computer", "stock": 3, "description": "High-performance laptop for work and gaming."},
    "C002": {"name": "Computer", "price": 117010, "photo": "C002.jpg", "category": "Computer", "stock": 2, "description": "Powerful desktop PC with Intel Core i9 processor."},
    "C003": {"name": "pant", "price": 10, "photo": "C002.jpg", "category": "Computer", "stock": 2, "description": "Powerful desktop PC with Intel Core or."},
    "C004": {"name": "tshet", "price": 110, "photo": "C002.jpg", "category": "cloth", "stock": 2, "description": "PCore i9 processor."},
}

CATEGORIES = list(set(product["category"] for product in PRODUCTS.values()))
CATEGORIES = list(set(product["category"] for product in PRODUCTS.values()))



@bot.message_handler(commands=['start'])


def agree(message):

      # Create a file in the current working directory (Google Colab environment)
 

      #files.download("/content/info.txt")


      chat_id = message.chat.id

      agreement_text = (
          "📝 Payment Agreement & Terms of Service\n\n"

            "📍 Applies To: All transactions made through BOT\n\n"


          "1. Payment Methods\n\n"
          "We accept the following payment options:\n"
          "✅ Telebirr – Payments can be made to number\n"
          "✅ Awash Bank – Payments can be deposited to Account No: 1234567890\n\n"

            "- 1.1 Payment Confirmation\n\n"
            "💠 Customers must send the transaction ID or a payment screenshot after completing payment.\n"
            "💠 Orders will only be processed after payment confirmation.\n\n"
          "2. Order Processing & Delivery\n\n"
            "💠 After payment verification, we will begin processing your order.\n"
            "💠 Estimated delivery times will be communicated to the customer.\n"
            "💠 We are not responsible for delays caused by third-party couriers or external factors such as weather, strikes, or government restrictions.\n\n"

          "3. Refund & Cancellation Policy\n\n"
            "- 3.1 Full Refund Policy\n\n"
            "✴ If your order cannot be delivered, you will receive a 100% refund within 24 hours.\n"
            "✴ Refunds will be made through the same payment method used for the transaction.\n\n"
            "- 3.2 Cancellation by Customer\n\n"
            "✴ Orders can only be canceled before shipment starts.\n"
            "✴ If canceled after shipment, a partial refund may apply (excluding delivery costs).\n\n"
            "- 3.3 Non-Refundable Cases\n\n"
            "✴ If a customer provides incorrect delivery information leading to failed delivery.\n"
            "✴ If a product is damaged due to customer handling after delivery.\n\n"

            "4. Fraud Prevention & Legal Compliance\n\n"
              "🔅 Any attempt to commit fraud (fake transactions, chargebacks, etc.) will result in a ban from our service and may be reported to authorities.\n"
              "🔅 Customers must use their real name and valid contact details to place orders.\n"
              "🔅 We comply with Ethiopian e-commerce and payment regulations.\n\n"

              "5. Customer Support & Dispute Resolution\n\n"
                  "🔅 If you have payment issues or disputes, contact our support team first: @market_Managebot\n"
                  "We will attempt to resolve disputes within 3 business days.\n\n"
                  "If a resolution is not reached, disputes may be handled under Ethiopian consumer protection laws.\n\n"
                  "🤝 By making a payment through ቅዳሜ ገበያ, you agree to these terms.\n"
                  "✨ For inquiries, contact support: @market_Managebot\n"



      )

      # Create an inline keyboard with a confirmation button
      keyboard = InlineKeyboardMarkup()
      confirm_button = InlineKeyboardButton("✅ I Agree & Continue 🫂", callback_data="agree_payment")
      keyboard.add(confirm_button)

      bot.send_message(chat_id, agreement_text, reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: call.data == "agree_payment")
def handle_agreement_confirmation(call):
    bot.answer_callback_query(call.id, "✅ Agreement Accepted!")
    bot.send_message(call.message.chat.id, "🎉 You can now proceed with your order!")
    start(call.message)









def start(message):
      
      markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
      button1 = KeyboardButton("ELECTRO 🔌")
      button2 = KeyboardButton("CLOTHE 👕")
      button3 = KeyboardButton("CAR 🚘")
      button4 = KeyboardButton("FOOD 🥘")

      button5 = KeyboardButton("Toys & Games 🎲")
      button6 = KeyboardButton("DECOR 🪑")

      button7 = KeyboardButton("BOOKS 📚")
      button8 = KeyboardButton("HOUSE 🛖")
      button9 = KeyboardButton("COSMO 💄")

      button10 = KeyboardButton("AGREEMENTS 🤝")
      button11 = KeyboardButton("HELP 🆘")
      markup.add(button1, button2, button3, button4, button6 , button7, button8, button9,button5, button10, button11)

      bot.send_message(message.chat.id, "ምድቦች", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["ELECTRO 🔌", "CLOTHE 👕", "CAR 🚘", "FOOD 🥘", "Toys & Games 🎲", "DECOR 🪑", "BOOKS 📚", "HOUSE 🛖","COSMO 💄", "AGREEMENTS 🤝", "HELP 🆘"])
def handle_reply(message):
 
    if message.text == "ELECTRO 🔌":
        chat_id = message.chat.id


        print("You selected ELECTRONICS 🦾")
        ele(message)

    elif message.text == "CLOTHE 👕":
        chat_id = message.chat.id


        cloth(message)
       

def cloth(message):
    
    chat_id = message.chat.id
    markup = InlineKeyboardMarkup()

    for category in CATEGORIES:
        markup.add(InlineKeyboardButton(category, callback_data=f"cloth_{category}"))

    bot.send_message(chat_id, "🛒 *Select a cloth Category:*", parse_mode="Markdown", reply_markup=markup)




def ele(message):
    chat_id = message.chat.id
    markup = InlineKeyboardMarkup()

    for category in CATEGORIES:
        markup.add(InlineKeyboardButton(category, callback_data=f"category_{category}"))

    bot.send_message(chat_id, "🛒 *Select a Electronics Category:*", parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith("category_"))
def show_products(call):
    chat_id = call.message.chat.id
    category = call.data.split("_")[1]

    markup = InlineKeyboardMarkup()
    for product_id, details in PRODUCTS.items():
        if details["category"] == category:
            markup.add(InlineKeyboardButton(details["name"], callback_data=f"product_{product_id}"))

    bot.send_message(chat_id, f"📦 *Available {category} Products:*", parse_mode="Markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("product_"))
def show_product_details(call):
    chat_id = call.message.chat.id
    product_id = call.data.split("_")[1]
    details = PRODUCTS.get(product_id)

    if not details:
        bot.send_message(chat_id, "❌ Product not found.")
        return

    product_info = f"""
🛍️ *{details['name']}*
💰 Price: {details['price']} ETB
📦 Stock: {details['stock']}
ℹ️ {details['description']}
"""
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🛒 Order Now", callback_data=f"order_{product_id}"))

    try:
        with open(details["photo"], "rb") as photo:
            bot.send_photo(chat_id, photo, caption=product_info, parse_mode="Markdown", reply_markup=markup)
    except Exception as e:
        bot.send_message(chat_id, f"⚠️ Failed to load image for {details['name']}.\n{product_info}", parse_mode="Markdown", reply_markup=markup)
        print(f"Error with {details['name']}: {e}")


# Delivery fees dictionary
DELIVERY_FEES = {
    "Addis Ababa": 200,
    "Bishoftu": 100,
    "Adama": 300,
    "Hawassa": 400,
    "Other": 500,
}



# Dictionary to store user data temporarily
user_data1 = {}



#@bot.callback_query_handler(func=lambda call: call.data.startswith("order_"))


@bot.callback_query_handler(func=lambda call: call.data.startswith("order_"))
def get_product_code(call):
    chat_id = call.message.chat.id
    product_code = call.data.split("_")[1]  # Extract product code from callback data

    user_data1[chat_id] = {"product_code": product_code}  # Store product code automatically

    product_info = PRODUCTS.get(product_code, {"name": "Unknown", "price": 0})  # Fetch product details

  #  bot.send_message(chat_id, f"🔢 *Product Code:* {product_code} ✅\n📦 *Product:* {product_info['name']}\n💰 *Price:* {product_info['price']} ETB")
    bot.send_message(chat_id, "👤 *Enter your full name:*")
    bot.register_next_step_handler(call.message, get_phone)

def get_phone(message):
    chat_id = message.chat.id
    user_data1[chat_id]["name"] = message.text  # Store name

    bot.send_message(chat_id, "📞 *Enter your phone number:*")
    bot.register_next_step_handler(message, get_location)

def get_location(message):
    chat_id = message.chat.id
    user_data1[chat_id]["phone"] = message.text  # Store phone number

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for city in DELIVERY_FEES.keys():
        keyboard.add(KeyboardButton(city))

    bot.send_message(chat_id, "📍 *Select your delivery location:*", reply_markup=keyboard)
    bot.register_next_step_handler(message, calculate_total_price)

def calculate_total_price(message):
    chat_id = message.chat.id
    location = message.text
    user_data1[chat_id]["location"] = location  # Store location

    product_code = user_data1[chat_id]['product_code']
    product_info = PRODUCTS.get(product_code, {"name": "Unknown", "price": 0})  # Get product info

    delivery_fee = DELIVERY_FEES.get(location, DELIVERY_FEES["Other"])
    total_price = product_info["price"] + delivery_fee  # Calculate total cost

    final_messagesus = (
    

        f"🔢 **Product Code:** {product_code}\n"
        f"📦 **Product:** {product_info['name']}\n"
        f"👤 **Name:** {user_data1[chat_id]['name']}\n"
        f"📞 **Phone:** {user_data1[chat_id]['phone']}\n"
        f"📍 **Location:** {location}\n"
        f"🤑 **Price:** {product_info['price']} Birr\n"
        f"🚚 **Delivery Fee:** {delivery_fee} Birr\n"
        f"💰 **Total Amount:** {total_price} Birr\n\n"
    )

    final_message = (
        f"📜 *Order Summary:*\n\n"
        f"🔢 **Product Code:** {product_code}\n"
        f"📦 **Product:** {product_info['name']}\n"
        f"👤 **Name:** {user_data1[chat_id]['name']}\n"
        f"📞 **Phone:** {user_data1[chat_id]['phone']}\n"
        f"📍 **Location:** {location}\n"
        f"🤑 **Price:** {product_info['price']} Birr\n"
        f"🚚 **Delivery Fee:** {delivery_fee} Birr\n"
        f"💰 **Total Amount:** {total_price} Birr\n\n"
    )



    # Create a receipt file
    file_name = f"receipt_{chat_id}.txt"
    with open(file_name, "w") as file:
        file.write(final_messagesus)
   
    # Send receipt file to user
    with open(file_name, "rb") as file:
        bot.send_document(sam_chat_id, file)
       bot.send_message(sam_chat_id, f"📩 *New Order Received!*\n\n{final_message}")

    bot.send_message(chat_id, final_message)

    bot.send_message(sam_chat_id, f"📩 *New Order Received!*\n\n{final_messagesus}")

    # Send confirmation buttons
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("YES 🙂‍↕️", callback_data="ookk")
    button2 = InlineKeyboardButton("Cancel 🙂‍↔️", callback_data="nnoo")
    markup.add(button1, button2)

    bot.send_message(chat_id, "🔹 *Please Confirm your order *", reply_markup=markup)











@bot.callback_query_handler(func=lambda call: call.data.startswith("oorder_"))
def order_product(call):
    chat_id = call.message.chat.id
    product_id = call.data.split("_")[1]
    details = PRODUCTS.get(product_id)

    if not details:
        bot.send_message(chat_id, "❌ Product not found.")
        return

    bot.send_message(chat_id, f"✅ Order received for *{details['name']}*! 🛍️\nOur team will contact you soon.", parse_mode="Markdown")

bot.polling()
