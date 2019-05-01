// Utilities
function dataURLToBlob(e){if(-1==e.indexOf(";base64,")){var t=(o=e.split(","))[0].split(":")[1],n=decodeURIComponent(o[1]);return new Blob([n],{type:t})}t=(o=e.split(";base64,"))[0].split(":")[1];for(var o,r=(n=window.atob(o[1])).length,a=new Uint8Array(r),i=0;i<r;++i)a[i]=n.charCodeAt(i);return new Blob([a],{type:t})}


// Main
console.log('wassup foo');
const igMinImgRatio = 0.8;
const igMaxImgRatio = 1.91;
const igOGImgRatio = 1;

var img = document.getElementById('id_image');
var resizedImgCanvas = document.createElement('canvas');

// append canvas
img.parentNode.insertBefore(resizedImgCanvas, img.nextSibling);

// handle onchange/input
img.onchange = function (e) {
    console.log('image added');
    var file = e.target.files[0];

    // Load the image
    var reader = new FileReader();
    reader.onload = function (readerEvent) {
        var image = new Image();
        image.onload = function (imageEvent) {

            // Resize the image
            var canvas = resizedImgCanvas;
            var maxImgWidth = 800;  // max width of final img
            var minImgWidth = 640;
            
            var width = image.width;
            var height = image.height;
            var ratio = width/height;

            console.log(width, height, ratio);


            // check min/max image dimensions & adjust
            if (width > maxImgWidth) {
                width = maxImgWidth;
            } else if (width < minImgWidth) {
                width = minImgWidth;
            }
            height = width * (1/ratio);

            // check ratio & adjust
            var canvasRatioToUse;  // we will fit the image within this.
            if (ratio >= igMinImgRatio && ratio <= igMaxImgRatio) {
                console.log('we should not resize');
                maxImgWidth = width;
                canvasRatioToUse = ratio;
            } else {
                console.log('we should resize');
                var isTooWide = (ratio > igMaxImgRatio);
                if (isTooWide) {
                    canvasRatioToUse = igMaxImgRatio;
                } else {
                    canvasRatioToUse = igMinImgRatio;
                }
            }

            canvas.width = width;
            canvas.height = width * (1/canvasRatioToUse);
            var context = canvas.getContext('2d');
            console.log('before');
            console.log('img', width, height, ratio);
            console.log('cnv', canvas.width, canvas.height, canvasRatioToUse);
            // make sure image will fit within canvas or adjust.
            if (height > canvas.height) {
                width = width * (canvas.height / height);
                height = canvas.height;
            }
            var canvasCenterX = Math.abs((canvas.width - width)/2);
            var canvasCenterY = Math.abs((canvas.height - height)/2);

            console.log('after');
            console.log('img', width, height, ratio);
            console.log('cnv', canvas.width, canvas.height, canvasRatioToUse);
            console.log(
                canvasCenterX,
                canvasCenterY
            );

            var bgColor = [51, 51, 51];
            // fill BG
            context.fillStyle = 'rgb(' + bgColor[0] + ', ' + bgColor[1] + ', ' + bgColor[2] + ')';
            context.imageSmoothingEnabled = false;
            context.drawImage(image, 0, 0, canvas.width, canvas.height);
            context.globalAlpha = 0.8;
            context.fillRect(0, 0, canvas.width, canvas.height);
            context.restore();
            context.globalAlpha = 1;
            context.imageSmoothingEnabled = true;


            // draw image at center of canvas
            context.drawImage(image, canvasCenterX, canvasCenterY, width, height);
            
            // get canvas data
            var dataUrl = canvas.toDataURL('image/jpeg');
            var resizedImage = dataURLToBlob(dataUrl);
            document.querySelector('#id_image_base64_text').value = dataUrl;
            console.log(dataUrl, resizedImage);
        }
        image.src = readerEvent.target.result;
    }
    reader.readAsDataURL(file);
}