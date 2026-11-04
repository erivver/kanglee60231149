
const swimmer = document.querySelector('.swimmer');
const head = document.querySelector('.circle');
const fish = document.querySelector('.fish');
const animations = document.querySelector('.motion').getAnimations({subtree:true});
const state = { x: innerWidth/2, y: innerHeight*.57, angle: 0,
  target: null, wait: 2, paused: false, eaten: 0, hunting: false, roam: null };
function setSpeed(hunting) {
  state.hunting = hunting;
  // Change playback rate without restarting the CSS animation's phase.
  animations.forEach(animation => animation.updatePlaybackRate(hunting ? 4 : 1));
  document.body.dataset.mode = hunting ? 'hunting' : 'idle';
}
function spawn() {
  const margin = 48;
  let x, y;
  for (let i=0; i<20; i++) {
    x = margin + Math.random()*Math.max(0,innerWidth-margin*2);
    y = innerHeight*.44 + Math.random()*Math.max(0,innerHeight*.34);
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
        state.wait = 2.5+Math.random()*2.5; state.roam = null;
        setSpeed(false);
      }
    } else {
      // Wander from the current position rather than returning to the center.
      if (!state.roam || Math.hypot(state.roam.x-state.x,state.roam.y-state.y)<40) {
        const marginX = Math.min(180, innerWidth*.3);
        const marginY = Math.min(180, innerHeight*.3);
        state.roam = {
          x: marginX+Math.random()*Math.max(0,innerWidth-marginX*2),
          y: innerHeight*.46+Math.random()*(innerHeight*.28)
        };
      }
      const dx = state.roam.x-state.x, dy = state.roam.y-state.y;
      const desired = Math.atan2(dy,dx)+Math.PI/2;
      const delta = Math.atan2(Math.sin(desired-state.angle),Math.cos(desired-state.angle));
      state.angle += delta*Math.min(1,dt*1.8);
      state.x += Math.sin(state.angle)*65*dt;
      state.y -= Math.cos(state.angle)*65*dt;
      state.x = Math.max(44,Math.min(innerWidth-44,state.x));
      state.y = Math.max(44,Math.min(innerHeight-44,state.y));
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
  state.roam = null;
  if (state.target) {
    state.target.x = Math.max(24,Math.min(innerWidth-24,state.target.x));
    state.target.y = Math.max(24,Math.min(innerHeight-24,state.target.y));
    fish.style.left=state.target.x+'px'; fish.style.top=state.target.y+'px';
  }
});
setSpeed(false); draw(); requestAnimationFrame(frame);
