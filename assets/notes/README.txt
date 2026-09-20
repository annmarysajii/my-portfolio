GUESTBOOK NOTES

Visitors write a note in the guestbook panel (footer link "Leave a note in the guestbook", or from the sticker book).

WITH SUPABASE (once it is set up; see supabase/setup.sql)
  * The note goes into a database table (guestbook_notes) as NOT approved, and you get an email heads-up (through FormSubmit).
  * To put a note on the wall: Supabase dashboard > Table Editor > guestbook_notes > tick "approved" on the row. It is on the wall within
    a minute. Nothing to paste, nothing to push. To take one down, untick it (or delete the row).
  * The two values the site needs (project URL and the anon / publishable key) go at the top of the guestbook code, in "const SB".
    They are public by design. NEVER put the service_role / secret key anywhere in the site.

WITHOUT IT (or as a way to pin a favourite by hand)
  * Add an entry to notes.json. Notes there are always shown first, then the approved ones from the database:

[
  { "name": "Mei", "text": "The stamps are so satisfying.", "colour": "yellow", "date": "2026-09-21" }
]

  colour is one of: yellow, pink, blue, green. name and date are optional. Keep each text under 240 characters. Commit and push.
