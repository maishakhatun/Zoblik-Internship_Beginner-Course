#Exercise 2: Understanding LEGB Rule
#This exercise demonstrates how Python searches for variables in different scopes.

'''
👉 Try it Yourself:

In the confirm_details function, comment out the line meeting_room = "Small Huddle Space 💡". 
What happens to the output for "Inside confirm_details"? Does it now use the meeting_room from schedule_meeting? 
This demonstrates the 'Enclosing' scope of LEGB!
Change the global meeting_room value. Observe how it only affects the output outside the schedule_meeting function.
'''


# Global variable: The default meeting room at Zoblik HQ
meeting_room = "Conference Room Alpha 🏢"

def schedule_meeting(meeting_name):
    # Enclosing (or Local to this function): Specific room for this type of meeting
    meeting_room = "Team Collaboration Hub 🤝"

    def confirm_details():
        # Local to this nested function: A last-minute change for THIS confirmation
        # If this line is commented, Python would look in the enclosing 'schedule_meeting' scope
        meeting_room = "Small Huddle Space 💡"
        print(f"  Inside confirm_details: Meeting '{meeting_name}' will be in {meeting_room}.")

    print(f"Inside schedule_meeting: Initial room for '{meeting_name}' is {meeting_room}.")
    confirm_details()

print("--- Zoblik Meeting Schedule ---")
print(f"Default global meeting room: {meeting_room}")

schedule_meeting("Weekly Sync")
print(f"After scheduling 'Weekly Sync': Default global meeting room is still: {meeting_room}")

schedule_meeting("Client Presentation")
print(f"After scheduling 'Client Presentation': Default global meeting room is still: {meeting_room}")
