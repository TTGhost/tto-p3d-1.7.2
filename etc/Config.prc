load-display pandagl

win-origin 50 50
win-size 800 600

fullscreen #f

framebuffer-mode rgba double-buffer depth hardware

notify-level warning
default-directnotify-level warning

model-path    models/
sound-path    models/
texture-path  models/

want-directtools  #f
want-tk           #f
want-pstats            #f
show-frame-rate-meter  #f

audio-library-name fmod_audio
hardware-animated-vertices 0

window-title Toontown

game-server 127.0.0.1
download-server http://s3.amazonaws.com/ttadls/
eventlog-host 127.0.0.1
server-version sv1.0.1

want-dev #f

audio-library-name p3fmod_audio
accountdb-local-file databases/csm-cookies.db

model-path ../models
default-model-extension .bam
icon-filename icon.ico
cursor-filename toonmono.cur

default-directnotify-level info

show-total-population #t
want-mat-all-tailors #t
estate-day-night #t
estate-goon #t
want-news-page #f
want-news-tab #f
want-housing #t
want-old-fireworks #t
want-instant-parties #t
want-silly-meter #t
want-game-tables #t
want-chinese-checkers #t
want-checkers #t
want-find-four #t
want-top-toons #t
want-golf-karts #t
want-parties #t
want-new-pat #f

#Disney Characters
want-classic-chars #t
want-mickey #t
want-donald-dock #t
want-daisy #t
want-minnie #t
want-pluto #t
want-donald-dreamland #t
want-chip-and-dale #t
want-goofy #t

#Server
allow-secret-chat #t
secret-chat-needs-parent-password #f
parent-password-set #t

holiday-list 64,65,66

ai-sleep .05
log-stack-dump #f

account-db-type local
force-black-cat-mgr #t
want-instant-delivery #t
