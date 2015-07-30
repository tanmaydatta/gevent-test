var socket = io.connect("/chat");
socket.on('connect', function () {
    alert('connected');
    $('#chat').addClass('connected');
});  
// socket.emit('join', 'tanmay'); 
socket.on('test', function (msg) {
    $('#response').html(msg);
    alert('test');
});
// alert('hello');
$('#login').submit(function(event){
	event.preventDefault();
	socket.emit('nickname',$('#login-input').val());
});

$('#msg').submit(function(event){
	event.preventDefault();
	socket.emit('msg',$('#message').val());
});
