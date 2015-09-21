from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin
from socketio.sdjango import namespace
import pdb

@namespace('/socket_chat')
class ChatNamespace(BaseNamespace, RoomsMixin, BroadcastMixin):
    nicknames = []

    # def initialize(self):
        # pdb.set_trace()
        # self.emit('test', 'hello ')
        
    def on_join(self, name):
        # self.room = room
        # self.join(room)
        self.emit('test', 'hello ' + name)

        # pkt = dict(type="event",
                   # name='test',
                   # args='hello',
                   # endpoint=self.ns_name)
        # for sessid, socket in self.socket.server.sockets.iteritems():
            # socket.send_packet(pkt)

        # pdb.set_trace()
        return True
        
    def on_nickname(self, nickname):
        # self.log('Nickname: {0}'.format(nickname))
        self.nicknames.append(nickname)
        self.socket.session['nickname'] = nickname
        for sessid, socket in self.socket.server.sockets.iteritems():
            print socket.session
        # print self.socket.session
        # self.broadcast_event('announcement', '%s has connected' % nickname)
        # self.broadcast_event('nicknames', self.nicknames)
        return True, nickname

    def recv_disconnect(self):
        # Remove nickname from the list.
        self.log('Disconnected')
        nickname = self.socket.session['nickname']
        self.nicknames.remove(nickname)
        self.broadcast_event('announcement', '%s has disconnected' % nickname)
        self.broadcast_event('nicknames', self.nicknames)
        self.disconnect(silent=True)
        return True

    def on_msg(self, msg, *args):
        # self.log('User message: {0}'.format(msg))
        # print 'hello'
        # for sessid, socket in self.socket.server.sockets.iteritems():
            # socket.send_packet(pkt)
        # self.broadcast_event('test', msg)
        # args = msg
        # pdb.set_trace()
        to = args[0]
        arg = [{'msg':msg,'user':self.socket.session['nickname']},self.socket.session['nickname']]
        arg = tuple(arg)
        print arg
        pkt = dict(type="event",
               name='test',
               args=arg,
               endpoint=self.ns_name)
        for sessid, socket in self.socket.server.sockets.iteritems():
            if to == socket.session['nickname']:
                socket.send_packet(pkt)
                # break
        print 'done'
        # print msg
        # self.emit('test',self.socket.session['nickname'] +':' +msg);
        return True

def socketio_service(request):
    socketio_manage(request.environ, {'/chat': ChatNamespace}, request)
    return 'out'