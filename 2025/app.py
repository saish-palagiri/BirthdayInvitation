import streamlit as st
import streamlit.components.v1 as components

# Set Streamlit page to wide layout
st.set_page_config(page_title="Birthday Invitation", layout="wide")

# HTML content as a string
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Birthday Invitation</title>
<link href="https://fonts.googleapis.com/css2?family=Kalam:wght@300;400;700&family=Rancho&display=swap" rel="stylesheet">
<style>
html, body {
  margin: 0;
  padding: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  font-family: 'Kalam', cursive;
  background: linear-gradient(135deg, #8B0000, #400000);
  color: #FFD700;
}

body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

h1 {
  font-family: 'Rancho', cursive;
  font-size: 5vw;
  margin: 1vw 0;
  text-shadow: 2px 2px 10px rgba(0,0,0,0.6);
}

p { font-size: 2vw; margin: 1vw 0 2vw; }

.btn {
  display: inline-block;
  padding: 1.5vw 3vw;
  border-radius: 12px;
  background: linear-gradient(135deg, #FF0000, #FF4500, #FF6347);
  color: #FFF;
  font-weight: bold;
  font-size: 1.5vw;
  text-decoration: none;
  transition: 0.3s;
  box-shadow: 0 0.5vw 1vw rgba(0,0,0,0.3);
  border: 0.2vw dashed #FFD700;
  margin-top: 2vw;
}

.btn:hover { transform: scale(1.08) rotate(-2deg); box-shadow: 0 0.8vw 2vw rgba(0,0,0,0.4); }

.details { margin-top: 2vw; font-size: 1.5vw; }
.details p { margin: 0.5vw 0; }

canvas#confetti {
  position: absolute;
  top:0; left:0;
  width:100%;
  height:100%;
  pointer-events:none;
  z-index:2;
}

/* Responsive for mobile */
@media (max-width: 768px) {
  h1 { font-size: 8vw; }
  p, .details { font-size: 4vw; }
  .btn { font-size: 4vw; padding: 3vw 5vw; }
}

@media (max-width: 480px) {
  h1 { font-size: 10vw; }
  p, .details { font-size: 5vw; }
  .btn { font-size: 5vw; padding: 4vw 6vw; }
}
</style>
</head>
<body>

<canvas id="confetti"></canvas>

<h1>You're Invited! To Saish 11th Birthday Party</h1>
<p>Join us for an unforgettable celebration!</p>
<a class="btn" href="https://docs.google.com/forms/d/16nrhMrfvONP2GqsTfJQzT1OiyuANxWdS_Qoh_zlyBqc/viewform" target="_blank">RSVP</a>

<div class="details">
  <p><strong>Date:</strong> September 6, 2025</p>
  <p><strong>Time:</strong> 3:00 PM (Reach By 2:55)</p>
  <p><strong>Location:</strong> 350 Talcottville Rd, Vernon, CT 06066</p>
</div>

<script>
const confettiCanvas = document.getElementById('confetti');
const ctx = confettiCanvas.getContext('2d');

function resizeCanvas() {
  confettiCanvas.width = window.innerWidth;
  confettiCanvas.height = window.innerHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

const confettiCount = 150;
const confetti = [];
for(let i=0; i<confettiCount; i++){
  confetti.push({
    x: Math.random()*confettiCanvas.width,
    y: Math.random()*confettiCanvas.height - confettiCanvas.height,
    r: Math.random()*6+4,
    d: Math.random()*confettiCount,
    color: `hsl(${Math.random()*10},100%,60%)`,
    tilt: Math.random()*10-10,
    tiltAngleIncrement: Math.random()*0.07+0.05,
    tiltAngle:0
  });
}

function drawConfetti(){
  ctx.clearRect(0,0,confettiCanvas.width,confettiCanvas.height);
  confetti.forEach(c=>{
    ctx.beginPath();
    ctx.lineWidth=c.r/2;
    ctx.strokeStyle=c.color;
    ctx.moveTo(c.x+c.tilt+c.r/4,c.y);
    ctx.lineTo(c.x+c.tilt,c.y+c.tilt+c.r/2);
    ctx.stroke();
  });
  updateConfetti();
}

function updateConfetti(){
  confetti.forEach(c=>{
    c.tiltAngle+=c.tiltAngleIncrement;
    c.y+=(Math.cos(c.d)+3+c.r/2)/2;
    c.tilt=Math.sin(c.tiltAngle)*15;
    if(c.y>confettiCanvas.height){
      c.x=Math.random()*confettiCanvas.width;
      c.y=-20;
      c.tilt=Math.random()*10-10;
    }
  });
}
setInterval(drawConfetti,20);
</script>

</body>
</html>
"""

# Render in Streamlit with a reasonable height
components.html(html_code, height=800, scrolling=False)
