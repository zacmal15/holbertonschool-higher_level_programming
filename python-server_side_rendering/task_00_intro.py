#!/usr/bin/python3
"""This module generates invitation files from a template"""


def generate_invitations(template, attendees):
    """Generate a separate invitation file for each attendee."""

    if not isinstance(template, str):
        print(
            "Invalid input: template must be a string, "
            "received {}.".format(type(template).__name__)
        )
        return
    
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Invalid input: every attendee must be a dictionary.")
        return
    
    if template == "":
        print("Template is empty, no output files generated.")
        return
    
    if attendees == []:
        print("No data provided, no output files generated.")
    
    placeholders = [
        "name",
        "event_title",
        "event_date",
        "event_location"
    ]

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for placeholder in placeholders:
            value = attendee.get(placeholder)

            if value is None:
                value = "N/A"

            invitation = invitation.replace(
                "{" + placeholder + "}",
                str(value)
            )

        filename = "output_{}.txt".format(index)

        try:
            with open(filename, "w") as file:
                file.write(invitation)
        except OSError as error:
            print("Error writing {}: {}".format(filename, error))