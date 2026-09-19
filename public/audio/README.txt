Room sound for the hero and the desk (opt-in: the visitor turns it on with the speaker button in the nav).
Nothing is synthesised. Files are .mp3 (the loops also try .ogg).

MUSIC (loops, about -18 LUFS, last 3s crossfaded into the first 3s so the loop has no click)
  day-music.mp3     Jazz Rainy Lounge, Alex Morgan
  night-music.mp3   2 AM Lofi Chill Ambient, Music For Videos

EFFECT SLOTS: one per KIND of thing. To give a kind its own sound, drop  <name>-1.mp3  (and -2, -3, -4 for variety)
into this folder. The page plays any that exist, at random, never the same twice in a row. Until a slot has its own
file it uses the fallback below; a slot with neither stays silent. No code change is needed. Short, mono, peak about
-3 dBFS, no reverb, 0.2 to 1 second.

  slot            file name           where it plays                                              fallback until you add one
  paperPrint      paper-print-N       hovering a photo print or a work card, a download card      paper-1/2/3
  paperSheet      paper-sheet-N       hovering the big lead sheet, the About notebook page        paper-1/2/3
  paperSlip       paper-slip-N        hovering a taped scrap, sticky note, the ID card             paper-1/2/3
  tape            tape-N              (planned) tape peeled or pressed                            silent
  stamp           stamp-N             (planned) a rubber stamp landing when a stamp is earned      silent
  stickerPeel     sticker-peel-N      (planned) picking up a sticker                              silent
  stickerPlace    sticker-place-N     (planned) pressing a sticker down                           silent
  reward          reward-N            (planned) a small chime for a reward                        silent
  rewardFinal     reward-final-N      (planned) the last stamp                                    silent
  drawerOpen      drawer-open-N       the quick-look drawer and the About Studio Desk drawer      drawer-open.mp3
  drawerClose     drawer-close-N      the same, closing                                           drawer-close.mp3
  (lamp click)    lamp-click.mp3      the lamp switch                                              silent

Paper hover is deliberately rare now: a mouse only, once per object per 20 seconds, and never more than one paper
sound every 3.5 seconds anywhere.

The generic files (paper-1/2/3, drawer-open, drawer-close) were made from makigai_maimai-paper-245786.mp3 and
freesound_community-drawer-41055.mp3. Check each file's licence before the site goes public.
