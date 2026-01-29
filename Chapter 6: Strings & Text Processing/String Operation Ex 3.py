#Exercise 3: Dynamic Email Generation
#Zoblik wants to send out personalized promotional emails.



# Variables for the email content
recipient_name = "Micheal"
product_discount = "Zoblik Smart Speaker"
discount_percentage = 25
expiration_date = "March 1, 2026"
Coupon_code = "ZSS25"

# Task: Create a personalized promotional email using f-strings.
# The email should greet the recipient by name, mention the discounted product and percentage,
# and clearly state the expiration date of the offer.

# --- Your code goes here ---

promotional_email = f"""
Subject: Special Offer Just For You, {recipient_name}!

Dear {recipient_name},

Great news! As a valued Zoblik customer, we're excited to offer you a special {discount_percentage}% discount on our incredible {product_discount}!

This is your chance to upgrade and experience the best of Zoblik technology at a fantastic price.

Hurry, this exclusive offer expires on {expiration_date}.

Use the Coupon Code "ZSS25" to get 10% EXTRA discount.

Best regards,
The Zoblik Team
"""

print(promotional_email)                    