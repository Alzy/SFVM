var artistsLis = document.querySelectorAll('#artists-list li');
for (var i = 0; artistsLis.length; i++) {
    artistsLis[i].addEventListener('click', function (e) {
        this.classList.add('selected');
        document.querySelector('#active-artist-overlay').classList.remove('hidden');
    }, );
}