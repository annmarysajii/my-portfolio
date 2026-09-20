-- GUESTBOOK: the whole database side, in one file. Run it once: Supabase dashboard > SQL Editor > New query > paste this > Run.
-- It is safe to run again (it drops and recreates the rules, and never touches existing notes).
--
-- WHAT THE PUBLIC CAN DO (this is enforced by the database itself, not by the website's code):
--   * add a note: only the three columns name, text, colour. A note is always saved as NOT approved, whatever a visitor sends.
--   * read the notes that are approved. Never the unapproved ones.
--   * nothing else: no editing, no deleting, no approving, no reading of anything else.
-- WHAT ONLY YOU CAN DO (from the Supabase dashboard > Table Editor > guestbook_notes): read every note, and tick "approved" (or delete).
-- A note goes on the wall the moment you tick it; there is nothing to push or paste.
--
-- Extra guards, inside the database: at most 6 new notes a minute across the whole site, at most 300 waiting unapproved at once,
-- no links, and text is trimmed. If someone floods it, the worst case is that new notes are refused for a minute; nothing bad can appear.

create table if not exists public.guestbook_notes (
  id          bigint generated always as identity primary key,
  created_at  timestamptz not null default now(),
  name        text not null default '' check (char_length(name) <= 30),
  text        text not null check (char_length(text) between 3 and 240),
  colour      text not null default 'yellow' check (colour in ('yellow', 'pink', 'blue', 'green')),
  approved    boolean not null default false
);

alter table public.guestbook_notes enable row level security;
alter table public.guestbook_notes force row level security;

-- the visitor's key (anon) gets only these, and nothing on any other table is granted here
revoke all on public.guestbook_notes from anon, authenticated;
grant insert (name, text, colour) on public.guestbook_notes to anon;      -- only these columns: id, created_at and approved can never be set by a visitor
grant select on public.guestbook_notes to anon;                           -- which rows they may see is decided by the policy below

drop policy if exists "visitors can leave a note" on public.guestbook_notes;
create policy "visitors can leave a note" on public.guestbook_notes
  for insert to anon with check (approved = false);

drop policy if exists "visitors can read approved notes" on public.guestbook_notes;
create policy "visitors can read approved notes" on public.guestbook_notes
  for select to anon using (approved = true);
-- (there is deliberately no update or delete policy for visitors)

-- guards, run for every new note. SECURITY DEFINER so it can count ALL notes, including the ones a visitor may not read.
create or replace function public.guestbook_guard() returns trigger
language plpgsql security definer set search_path = '' as $$
begin
  new.name := btrim(new.name);
  new.text := btrim(new.text);
  if new.text ~* '(https?:|www\.|\.com\M)' or new.name ~* '(https?:|www\.|\.com\M)' then
    raise exception 'links are not allowed';
  end if;
  if (select count(*) from public.guestbook_notes where created_at > now() - interval '1 minute') >= 6 then
    raise exception 'too many notes right now, try again in a minute';
  end if;
  if (select count(*) from public.guestbook_notes where approved = false) >= 300 then
    raise exception 'the inbox is full for now';
  end if;
  return new;
end $$;

drop trigger if exists guestbook_guard_trg on public.guestbook_notes;
create trigger guestbook_guard_trg before insert on public.guestbook_notes
  for each row execute function public.guestbook_guard();

-- to check it worked (optional): run these two lines. The first should return nothing, the second one row.
--   select * from public.guestbook_notes;                      -- as you, in the SQL editor, you see everything
--   insert into public.guestbook_notes (name, text) values ('test', 'hello there');   -- then tick approved in the Table Editor
