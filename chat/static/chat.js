var socket = io.connect("/socket_chat");
socket.on('connect', function () {
    alert('connected');
    $('#chat').addClass('connected');
});  
// socket.emit('join', 'tanmay'); 
socket.on('test', function (msg) {
	console.log(msg);
    $('#response').html(msg['msg']);
    alert('test');
});
// alert('hello');
$('#login').submit(function(event){
	event.preventDefault();
	socket.emit('nickname',$('#login-input').val());
});

$('#msg').submit(function(event){
	event.preventDefault();
	// socket.emit('msg',{'ms':$('#message').val(),'mg':'test'});
	socket.emit('msg',$('#message').val(),'test');
});
