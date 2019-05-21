  const config = {
      playerContainer: document.getElementById("playem_video"),
  };

  // init playem and players
  var playem = new Playem();
  playem.addPlayer(AudioFilePlayer, config);
  playem.addPlayer(VimeoPlayer, config);

  // init logging for player events
  playem.on("onTrackChange", (data) => console.log("play track " + data.trackId));
  playem.on("onError", (data) => console.error("error:", data));

  // create a playlist
  playem.addTrackByUrl("https://archive.org/download/JeremyJereskyDrumLoop/drumLoop.mp3");
  playem.addTrackByUrl("vimeo.com/50872925");

  // wait for soundmanager to be ready before playing tracks
  soundManager.setup({ onready: () => playem.play() });
  soundManager.beginDelayedInit();