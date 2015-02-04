aux-display pandagl
aux-display pandadx9
aux-display pandadx8
aux-display pandadx7

load-file-type egg pandaegg
egg-object-type-portal          <Scalar> portal { 1 }
egg-object-type-polylight       <Scalar> polylight { 1 }
egg-object-type-seq24           <Switch> { 1 } <Scalar> fps { 24 }
egg-object-type-seq12           <Switch> { 1 } <Scalar> fps { 12 }
egg-object-type-indexed         <Scalar> indexed { 1 }
egg-object-type-model           <Model> { 1 }
egg-object-type-dcs             <DCS> { 1 }
egg-object-type-barrier         <Collide> { Polyset descend }
egg-object-type-sphere          <Collide> { Sphere descend }
egg-object-type-invsphere       <Collide> { InvSphere descend }
egg-object-type-tube            <Collide> { Tube descend }
egg-object-type-trigger         <Collide> { Polyset descend intangible }
egg-object-type-trigger-sphere  <Collide> { Sphere descend intangible }
egg-object-type-bubble          <Collide> { Sphere keep descend }
egg-object-type-ghost           <Scalar> collide-mask { 0 }
load-file-type ptloader
egg-object-type-direct-widget   <Scalar> collide-mask { 0x80000000 } <Collide> { Polyset descend }

cull-bin gui-popup 60 unsorted

paranoid-clock 1

window-title Toontown Online

###########################
# SERVER CONFIG
# DO NOT EDIT

# DIFFERENCES FROM DEV
# SERVER ACCOUNT TYPE

air-connect 127.0.0.1
eventlog-host 127.0.0.1
###########################

dc-file tth.dc
want-dev #f

accountdb-local-file databases/csm-cookies.db

model-path models/
default-model-extension .bam
icon-filename phase_3/etc/icon.ico
cursor-filename phase_3/etc/toonmono.cur

default-directnotify-level info

cog-thief-ortho 0
show-total-population #t
want-mat-all-tailors #t
estate-day-night #t
want-karts #t
want-pets #t
want-news-page #f
want-news-tab #f
want-housing #t
want-old-fireworks #t
want-instant-parties #t
want-silly-meter #t
want-game-tables #t
want-lawbot-cogdo #f
want-emblems #f

want-classic-chars #t
want-mickey #t
want-donald-dock #t
want-daisy #t
want-minnie #t
want-pluto #t
want-donald-dreamland #t
want-chip-and-dale #t
want-goofy #t

allow-secret-chat #t
secret-chat-needs-parent-password #f
parent-password-set #t

holiday-list 64,65,66

ai-sleep .01
log-stack-dump #f

account-db-type server
mega-invasion-shards 401 402
want-top-toons #t
ban-do-ban #t

forbid-surfers-game #t
metagame-min-2-players #f
