from pathlib import Path
p=Path('outputs/index.html');s=p.read_text()
s=s.replace('<title>Shark Motion</title>','<title>SHARK — Beneath the Silence</title>')
css='''
/* Cinematic poster composition */
body { font-family: Arial, Helvetica, sans-serif; }
main { overflow: hidden; isolation: isolate; background:
 radial-gradient(ellipse at 50% -18%, #dbf2e9 0, #a4d5df80 25%, transparent 56%),
 linear-gradient(180deg, #64b2d4 0%, #64b2d4 28%, #367f9c 53%, #123d50 76%, #03131f 100%); }
main::before { content:''; position:absolute; inset:-20%; z-index:-1; pointer-events:none;
 background: repeating-conic-gradient(from 163deg at 50% 0%, transparent 0deg 8deg, #d4f6ed12 9deg 12deg, transparent 13deg 21deg);
 filter:blur(14px); animation: light-drift 18s ease-in-out infinite alternate; }
main::after { content:''; position:absolute; inset:0; pointer-events:none; z-index:5;
 background:radial-gradient(ellipse at 50% 38%, transparent 35%, #000a 115%);
 box-shadow:inset 0 0 0 14px #061e2a22; }
.poster-top { position:absolute; top:30px; left:38px; right:38px; display:flex; justify-content:space-between;
 font-size:10px; font-weight:700; letter-spacing:.24em; color:#092b38; z-index:3; }
.shark-title { top:12vh; width:100%; text-align:center; font-size:clamp(100px,22vw,270px);
 letter-spacing:-.035em; font-style:normal; line-height:.82; color:#000; }
.shark-title span { transform:scaleX(1.08); }
.shark-title::after { display:none; }
.tagline { position:absolute; top:calc(12vh + clamp(100px,22vw,270px)*.82 + 26px); left:0; right:0;
 text-align:center; margin:0; color:#082633; font-size:11px; letter-spacing:.42em; z-index:3; }
.poster-footer { position:absolute; left:38px; right:38px; bottom:30px; z-index:6; color:#c4d9dc; text-align:center; pointer-events:none; }
.kicker { font-size:10px; letter-spacing:.38em; color:#7fadb9; margin:0 0 14px; }
.poster-line { font-size:clamp(16px,2vw,23px); font-weight:400; letter-spacing:.17em; margin:0 0 25px; }
.credits { border-top:1px solid #96c1cf33; padding-top:16px; display:flex; justify-content:space-between; align-items:center;
 font-size:9px; letter-spacing:.16em; color:#82a5b1; }
.credits strong { font-size:10px; color:#d1e4e7; letter-spacing:.25em; font-weight:400; }
.swimmer { z-index:1; filter:drop-shadow(12px 24px 16px #00172355); }
.circle { background:radial-gradient(circle at 30% 20%, #a9c2ca 0%, #708090 45%, #344956 100%);
 box-shadow:inset 0 1px 1px #e4f7ff55, inset -7px -10px 18px #0b243b33; }
.fish { z-index:2; background:#eee6c2; box-shadow:0 0 12px #fff2bb99, 0 0 45px #fff2bb33; }
.depth-label { position:absolute; left:38px; top:55%; writing-mode:vertical-rl; color:#b0d8e066; font-size:9px; letter-spacing:.35em; }
.hunt-status { position:absolute; right:38px; top:55%; width:4px; height:36px; background:#c9e4e433; transition:background .3s, box-shadow .3s; }
body[data-mode="hunting"] .hunt-status { background:#f1c39c; box-shadow:0 0 24px #f1c39c66; }
@keyframes light-drift { from {transform:translateX(-3%) rotate(-3deg)} to {transform:translateX(3%) rotate(3deg)} }
@media(max-width:600px) {
 .poster-top {left:22px; right:22px; top:24px; font-size:8px; letter-spacing:.12em;}
 .shark-title {top:17vh; font-size:27vw;}
 .tagline {top:calc(17vh + 22vw + 20px); font-size:8px; letter-spacing:.3em;}
 .poster-footer {left:22px;right:22px;bottom:24px;}
 .poster-line {font-size:16px;letter-spacing:.08em;}
 .credits {font-size:7px;letter-spacing:.05em;gap:12px;}
 .credits strong {font-size:8px;letter-spacing:.1em;}
 .depth-label {left:18px;} .hunt-status {right:18px;}
}
@media(prefers-reduced-motion:reduce) {main::before {animation:none;}}
'''
s=s.replace('</style>',css+'</style>')
s=s.replace('  <h1 class="shark-title">','  <div class="poster-top"><span>AN EXPERIMENT IN MOTION</span><span>VOL. 01 / 2026</span></div>\n  <h1 class="shark-title">')
s=s.replace('  <div class="swimmer">','  <p class="tagline">BENEATH THE SILENCE.</p>\n  <div class="depth-label" aria-hidden="true">THE DEEP IS NEVER STILL</div><div class="hunt-status" aria-hidden="true"></div>\n  <div class="swimmer">')
s=s.replace('</main>','''  <footer class="poster-footer">
    <p class="kicker">A LIVING POSTER</p>
    <p class="poster-line">고요함 아래, 본능이 깨어난다.</p>
    <div class="credits"><span>CONCEPT &amp; MOTION STUDY</span><strong>SHARK</strong><span>DESIGN ITS MOVEMENT</span></div>
  </footer>
</main>''')
s=s.replace('y: innerHeight/2-104','y: innerHeight*.57')
s=s.replace('y = margin + Math.random()*Math.max(0,innerHeight-margin*2);','y = innerHeight*.44 + Math.random()*Math.max(0,innerHeight*.34);')
s=s.replace('y: marginY+Math.random()*Math.max(0,innerHeight-marginY*2)','y: innerHeight*.46+Math.random()*(innerHeight*.28)')
for f in ['outputs/index.html','outputs/shark-motion.html','work/shark-motion/dist/index.html']:Path(f).write_text(s)
Path('work/check-motion.js').write_text(s.split('<script>')[1].split('</script>')[0])
