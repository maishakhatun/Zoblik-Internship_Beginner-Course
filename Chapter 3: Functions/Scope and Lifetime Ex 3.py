#Exercise 3: Using Default Arguments
#Let's practice making functions more flexible with default arguments.

def send_zoblik_notification(message, recipient="All Zoblik Employees", urgency="Normal", sender="HR Department"):
    """
    Sends a notification across Zoblik Inc.
    'message' is mandatory. 'recipient' and 'urgency' have default values.
    """
    print(f"Sending '{urgency}' notification to {recipient}:")
    print(f"Message: '{message}'")
    print(f"Sender: {sender}\n")

print("--- Zoblik Notification System ---")

# 1. Send a standard company-wide notification
send_zoblik_notification("Remember to submit your Q2 reports!")

# 2. Send an urgent notification to a specific department
send_zoblik_notification("Urgent security patch update!", recipient="IT Department", urgency="Urgent", sender="CTO Office")

# 3. Send a normal notification to a specific team
send_zoblik_notification("New coffee machine is installed!", recipient="Marketing Team")

# 4. Send an urgent, default-recipient message
send_zoblik_notification("Fire drill scheduled for 2 PM!", urgency="Urgent")