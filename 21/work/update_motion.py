from pathlib import Path
p=Path('outputs/shark-motion.html')
s=p.read_text().replace('--paper: #F4F1E8','--paper: #64b2d4')
s=s.replace('main { height: 100svh; min-height: 320px; display: grid; place-items: center; }','main { height: 100svh; position: relative; }\n.swimmer { position: absolute; left: 0; top: 0; transform-origin: 0 0; will-change: transform; }\n.fish { position: absolute; width: 16px; height: 16px; border-radius: 50%; background: #fff3ce; transform: translate(-50%, -50%); box-shadow: 0 0 16px #fff3ce55; }\n.fish[hidden] { display: none; }')
s=s.replace('.motion { display: flex;', '.motion { margin-left: -40px; margin-top: -40px; display: flex;')
s=s.replace('  <div class="motion"', '  <div class="swimmer"><div class="motion"')
s=s.replace('  </div>\n</main>', '  </div></div>\n  <div class="fish" role="img" aria-label="작은 먹이 원" hidden></div>\n</main>')
start=s.index('<script>'); end=s.index('</script>',start)
s=s[:start]+'''<script>
const swimmer = document.querySelector('.swimmer');
const head = document.querySelector('.circle');
const fish = document.querySelector('.fish');
const animations = document.querySelector('.motion').getAnimations({subtree:true});
const state = { x: innerWidth/2, y: innerHeight/2-104, angle: 0,
  target: null, wait: 2, paused: false, eaten: 0, hunting: false };
function setSpeed(hunting) {
  state.hunting = hunting;
  // Change playback rate without restarting the CSS animation's phase.
  animations.forEach(animation => animation.updatePlaybackRate(hunting ? 2 : 1));
  document.body.dataset.mode = hunting ? 'hunting' : 'idle';
}
function spawn() {
  const margin = 48;
  let x, y;
  for (let i=0; i<20; i++) {
    x = margin + Math.random()*Math.max(0,innerWidth-margin*2);
    y = margin + Math.random()*Math.max(0,innerHeight-margin*2);
    if (Math.hypot(x-state.x,y-state.y)>140) break;
  }
  state.target = {x,y};
  fish.style.left = x+'px'; fish.style.top = y+'px'; fish.hidden = false;
  setSpeed(true);
}
function draw() {
  swimmer.style.transform = `translate(${state.x}px, ${state.y}px) rotate(${state.angle}rad)`;
}
let previous;
function frame(now) {
  const dt = previous === undefined ? 0 : Math.min((now-previous)/1000, .04);
  previous = now;
  if (!state.paused) {
    if (state.target) {
      const dx = state.target.x-state.x, dy = state.target.y-state.y;
      const distance = Math.hypot(dx,dy);
      const desired = Math.atan2(dy,dx)+Math.PI/2;
      const delta = Math.atan2(Math.sin(desired-state.angle),Math.cos(desired-state.angle));
      state.angle += delta*Math.min(1,dt*8);
      const step = Math.min(distance,260*dt);
      if (distance>0) { state.x += dx/distance*step; state.y += dy/distance*step; }
      draw();
      const box = head.getBoundingClientRect();
      const hx = box.left+box.width/2, hy = box.top+box.height/2;
      // Use the actual animated front circle, with radius 40, against food radius 8.
      if (Math.hypot(hx-state.target.x,hy-state.target.y)<=48) {
        fish.hidden = true; state.target = null; state.eaten++;
        state.wait = 2.5+Math.random()*2.5;
        setSpeed(false);
      }
    } else {
      // Smoothly return to the original central arrangement after eating.
      const ease = 1-Math.exp(-dt*1.6);
      state.x += (innerWidth/2-state.x)*ease;
      state.y += (innerHeight/2-104-state.y)*ease;
      const delta = Math.atan2(Math.sin(-state.angle),Math.cos(-state.angle));
      state.angle += delta*ease;
      state.wait -= dt;
      if (state.wait<=0) spawn();
      draw();
    }
  }
  requestAnimationFrame(frame);
}
document.addEventListener('keydown', event => {
  if (event.code !== 'Space' || event.repeat) return;
  event.preventDefault(); state.paused = !state.paused;
  animations.forEach(a => state.paused ? a.pause() : a.play());
});
addEventListener('resize', () => {
  if (state.target) {
    state.target.x = Math.max(24,Math.min(innerWidth-24,state.target.x));
    state.target.y = Math.max(24,Math.min(innerHeight-24,state.target.y));
    fish.style.left=state.target.x+'px'; fish.style.top=state.target.y+'px';
  }
});
setSpeed(false); draw(); requestAnimationFrame(frame);
</script>'''+s[end+9:]
p.write_text(s)
Path('outputs/index.html').write_text(s)
Path('work/shark-motion/dist/index.html').write_text(s)
