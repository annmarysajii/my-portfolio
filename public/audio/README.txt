Room sound for the hero and the desk (opt-in: the visitor turns it on with the speaker button in the nav).
Nothing is synthesised. Files are .mp3 (the loops also try .ogg).

MUSIC (loops, about -18 LUFS, last 3s crossfaded into the first 3s so the loop has no click)
  day-music.mp3     Jazz Rainy Lounge, Alex Morgan
  night-music.mp3   2 AM Lofi Chill Ambient, Music For Videos

EFFECT SLOTS: one per KIND of thing. To give a kind its own sound, drop  <name>-1.mp3  (and -2, -3, -4 for variety)
into this folder. The page plays any that exist, at random, never the same twice in a row. Until a slot has its own
file it uses the fallback below; a slot with neither stays silent. No code change is needed. Short, mono, peak about
-3 dBFS, no reverb, 0.2 to 1 second.

  slot            file name           where it plays                                              files now
  paperPrint      paper-print-N       hovering a photo print or a work card, a download card      paper-print-1 (polaroid printing)
  paperSheet      paper-sheet-N       hovering the big lead sheet, the About notebook page        (none: uses paper-1/2/3)
  paperSlip       paper-slip-N        hovering a taped scrap, sticky note, the ID card             paper-slip-1 (paper slide)
  pageTurn        page-turn-N         turning the hero notebook's page                             page-turn-1
  tape            tape-N              tape peeled or pressed (planned)                             tape-1, tape-2 (duct tape)
  stamp           stamp-N             a rubber stamp: earned stamps, the notebook stamps, and     stamp-1
                                      any stamp pressed in the Draw toy
  stickerPeel     sticker-peel-N      picking up a sticker                                         sticker-peel-1, -2 (protective film)
  stickerPlace    sticker-place-N     pressing a sticker down                                      sticker-place-1 (soft thump)
  reward          reward-N            a small chime for a reward                                   reward-1
  rewardFinal     reward-final-N      the last stamp                                               reward-final-1
  drawerOpen      drawer-open-N       the quick-look drawer and the About Studio Desk drawer      drawer-open.mp3
  drawerClose     drawer-close-N      the same, closing                                            drawer-close.mp3
  toyBounce       toy-bounce-N        Animate: pressing a principle                                toy-bounce-1..3 (cartoon boing)
  toyClap         toy-clap-N          Capture: the clapper                                         toy-clap-1 (clack)
  toyDraw         toy-draw-N          Draw: the pen starting a stroke                              toy-draw-1..3 (pencil)
  (lamp click)    lamp-click.mp3      the lamp switch                                              lamp-click.mp3

The new files were cut, faded and level-matched with ffmpeg (mono, 44.1 kHz, peaks -3 to -8 dBFS) from the
recordings in assets/sound/, which are the untouched originals: polaroid printing, turn-a-page, paper-slide-short,
duct-tape-peels, peeling-off-protective-film, stamp, thump2, ui-chime-notification, magic-spell-03, light-switch,
cartoon_boing, clack and pencil. To use a different section of one, re-cut it from assets/sound/.

Paper hover is deliberately rare now: a mouse only, once per object per 20 seconds, and never more than one paper
sound every 3.5 seconds anywhere.

The generic files (paper-1/2/3, drawer-open, drawer-close) were made from makigai_maimai-paper-245786.mp3 and
freesound_community-drawer-41055.mp3. Check each file's licence before the site goes public.
