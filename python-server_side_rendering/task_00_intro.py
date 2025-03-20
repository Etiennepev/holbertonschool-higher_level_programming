#!/usr/bin/python3
"""Generates personalized invitation files"""
from os.path import exists

def generate_invitations(template, attendees):
    
    if not exists("template.txt"):
        raise FileNotFoundError("template.txt not found")
    
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list")
        return
    
    if not template:
        print("Error: Template can't be empty")
        return
    
    if not attendees:
        print("Error: Attendees list can't be empty")
        return


    for i, attendee in enumerate(attendees, start=1):
        invitations = template.format(
			name=attendee.get("name", "N/A"),
   			event_title=attendee.get("event_title", "N/A"),
   			event_date=attendee.get("event_date", "N/A"),
   			event_location=attendee.get("event_location", "N/A"),
		)
        filename = "output_{}.txt".format(i)
        
        with open(filename, "w", encoding="utf-8") as file:
            file.write(invitations)
        