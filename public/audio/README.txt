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
  drawerStrip     drawer-strip-N      hovering a paper strip in the open drawer: a soft thump      drawer-strip-1, -2 (thump)
  toyBounce       toy-bounce-N        Animate: pressing a principle                                toy-bounce-1..3 (cartoon boing)
  toyClap         toy-clap-N          Capture: the clapper                                         toy-clap-1 (clack)
  toyDraw         toy-draw-N          Draw: the pen starting a stroke                              toy-draw-1..3 (pencil)
  (lamp click)    lamp-click.mp3      the lamp switch                                              lamp-click.mp3

LEVELS AND TIMING (portfolio.html, initRoomSound)
  Every effect is decoded as soon as room sound is switched on, so a press plays immediately (no fetch on first use).
  Mouse presses on the toys and the notebook page sound on the press itself, not when the button comes back up.
  Base levels are --snd-ui .30 and --snd-rustle .13 (night .34 / .15); each kind then has its own trim in SLOT_VOL
  (for example reward .45, toyBounce .45, tape .7). A soft limiter sits on the output. To make one kind quieter or louder,
  change its number in SLOT_VOL. A fast second press cuts the first short instead of stacking on it, and each play is
  varied by a few percent in speed and volume so repeats do not sound identical.

The new files were cut, faded and level-matched with ffmpeg (mono, 44.1 kHz, peaks -3 to -8 dBFS) from the
recordings in assets/sound/, which are the untouched originals: polaroid printing, turn-a-page, paper-slide-short,
duct-tape-peels, peeling-off-protective-film, stamp, thump2, ui-chime-notification, magic-spell-03, light-switch,
cartoon_boing, clack and pencil. To use a different section of one, re-cut it from assets/sound/.

Paper hover is minimal on purpose: only a project card sounds (paperPrint) and a strip in the open drawer (drawerStrip, a soft thump), mouse only, the instant the pointer enters (never a delay; at most one hover sound per 200 ms, and a card stays quiet for 8 seconds
after it has sounded). No other sheet, slip or photo makes a hover sound (paperSheet and paperSlip
are unused for now).

The generic files (paper-1/2/3, drawer-open, drawer-close) were made from makigai_maimai-paper-245786.mp3 and
freesound_community-drawer-41055.mp3. Check each file's licence before the site goes public.
