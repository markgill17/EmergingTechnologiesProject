// Adpated from: https://www.html5canvastutorials.com/labs/html5-canvas-paint-application/

//Drawing on the canvas
// getting the canvas using the id tag
var canvas = document.getElementById('canvasID');
// creating var: ctx
var ctx = canvas.getContext('2d');

var painting = document.getElementById('canvasDiv');
var paint_style = getComputedStyle(painting);

// setting width and height to values set in html
canvas.width = parseInt(paint_style.getPropertyValue('width'));
canvas.height = parseInt(paint_style.getPropertyValue('height'));

// set mouse to 0, 0
var mouse = {x: 0, y: 0};

// offset mouse
canvas.addEventListener('mousemove', function (e) {
    mouse.x = e.pageX - this.offsetLeft;
    mouse.y = e.pageY - this.offsetTop;
}, false);

ctx.lineWidth = 10;
ctx.lineJoin = 'round';
ctx.linCap = 'round';
ctx.strokeStyle = '#FFFFFF';

canvas.addEventListener('mousedown', function (e) {
    ctx.beginPath();
    ctx.moveTo(mouse.x, mouse.y);
    canvas.addEventListener('mousemove', onPaint, false);
}, false);

canvas.addEventListener('mouseup', function (e) {
    canvas.removeEventListener('mousemove', onPaint, false);
}, false);

var onPaint = function () {
    ctx.lineTo(mouse.x, mouse.y);
    ctx.stroke();
};

// JQuery Methods ===========================================================
$('#resetBtn').click(function () {
    // the reset button clears the contents of the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
});

// Save the Canvas
$('#saveBtn').click(function () {
    // save button uses ajax to make a post request
    var canvas = document.getElementById("canvasID");
    var dataURL = canvas.toDataURL();
    console.log(dataURL);
    $.ajax({
        type: 'POST',
        url: '/predictDigit',
        data: {
            imgBase64: dataURL
        }
    }).done(function (data) {
        // console log for testing purposes
        console.log('SENT');
        $("#predictDigit").empty().append(data);
    });
});