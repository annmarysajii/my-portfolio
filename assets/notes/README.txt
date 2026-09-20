GUESTBOOK NOTES

Visitors write a note in the guestbook panel (footer link "Leave a note in the guestbook", or from the sticker book). It is sent to
annie10302004@gmail.com through FormSubmit, the same address the contact form uses, with the subject "New guestbook note". Nothing goes
on the wall until you have read it.

To put a note on the wall, add an entry to notes.json (newest last or first, whichever you like; the wall shows them in file order):

[
  { "name": "Mei", "text": "The stamps are so satisfying.", "colour": "yellow", "date": "2026-09-21" },
  { "name": "Jo",  "text": "Found all the Keep Yourself Safe doodles!", "colour": "pink", "date": "2026-09-22" }
]

colour is one of: yellow, pink, blue, green. name and date are optional. Keep each text under 240 characters. Commit and push, and it
appears on the wall. To take a note down, delete its entry.
