const video = document.getElementById('myVideo');
const music = document.getElementById("bgMusic");

video.addEventListener('loadedmetadata', () => {
  video.playbackRate = 0.4;
});

function setupFadeOut() {
  setTimeout(() => {
    const fadeInterval = setInterval(() => {
      if (music.volume > 0.05) {
        music.volume -= 0.04;
      } else {
        music.volume = 0.4;
        music.pause();
        clearInterval(fadeInterval);
      }
    }, 200);
  }, (55 - 2) * 1000);
}

music.currentTime = 7;
music.volume = 0.4;
music.play().then(() => {
  setupFadeOut();
}).catch(() => {
  console.log("Autoplay blocked. Will play on user interaction.");
});

document.addEventListener("click", () => {
  if (music.paused) {
    music.currentTime = 2;
    music.volume = 0.4;
    music.play().then(() => {
      setupFadeOut();
    }).catch(err => {
      console.log("Play failed:", err);
    });
  }
});

