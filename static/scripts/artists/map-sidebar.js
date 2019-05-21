var artists = document.querySelectorAll('#artists-list li');
var activeArtistOverlay = document.querySelector('#active-artist-overlay');
var activeArtistOverlayContent = activeArtistOverlay.querySelector('#active-artist-overlay .content');


function viewArtistDetails (artist) {
    artist.classList.add('selected');
    
    var details = artist.querySelector('.details');
    
    activeArtistOverlayContent.innerHTML = "";
    activeArtistOverlayContent.append(details || "");
    activeArtistOverlay.classList.remove('hidden');
}

function closeArtistDetails () {
    var selected = document.querySelectorAll('#artists-list li.selected');
    for (var i = 0; i < selected.length; i++) {
        selected[i].classList.remove('selected');
    }
    
    activeArtistOverlay.classList.add('hidden');
}


for (var i = 0; i < artists.length; i++) {
    artists[i].addEventListener('click', function (e) {
        viewArtistDetails(this);
    }, );
}