#🔄 Exercise 3: Practicing Loop Control (break and continue)
#Imagine you're reviewing a list of security logs from Zoblik's server. 
#You want to process most logs, but skip irrelevant ones and stop if a critical alert is found.

security_logs = [
    "INFO: User login successful",
    "DEBUG: Temp file cleaned",
    "ALERT: Unauthorized access attempt detected!",
    "INFO: Database backup complete",
    "DEBUG: Background task finished",
    "WARNING: Disk space low"
]

print("--- Analyzing Zoblik Security Logs ---")
for log_entry in security_logs:
    
    # Skip DEBUG and WARNING logs
    if "DEBUG" in log_entry or "WARNING" in log_entry:
        print(f"Skipping low priority log: {log_entry}")
        continue  # Skip to the next log entry
    
    # Stop if "User login successful" is found
    if "User login successful" in log_entry:
        print(f"User login detected: {log_entry}! Stopping analysis immediately!")
        break  # Exit the loop entirely
    
    # Process all other standard logs
    print(f"Processing standard log: {log_entry}")

print("--- Log analysis concluded. ---")
