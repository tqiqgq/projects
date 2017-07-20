import socket
import asyncore
import threading

scoreboard = {}
list_words = []
list_words.append('python')
game_bool = True


class Game_dispatcher(asyncore.dispatcher_with_send):
    Main_server = None

    def __init__(self, socket_game, server_game):
        asyncore.dispatcher_with_send.__init__(self, socket_game)
        self.sock = socket_game
        self.Main_server = server_game
        self.max_score = 5
        global list_words
        global game_bool
        self.socket.send(b'You connect to game Words! Welcome!\nMax score = ' + str(self.max_score).encode())
        nick_thread = threading.Thread(target=self.Main_server.create_nick(self.sock))
        nick_thread.start()
        # nick_thread.join()
        self.Main_server.send_all_except(
            '{} join to Game'.format(self.Main_server.client_nick.get(self.sock)),
            except_client=self.sock, server_message=True)
        if len(self.Main_server.client_nick.values()) >= 2:
            self.game_start()

    def handle_read(self):
        self.sock.setblocking(False)
        data = self.recv(1024)
        data = data.decode("utf-8")
        if game_bool:
            self.game_handle(data, self.sock)

    def game_start(self):
        self.Main_server.send_all_except("Game start!\n", self.sock, server_message=True)
        self.Main_server.send_all_except("First word -  python", self.sock, server_message=True)
        global scoreboard
        scoreboard = scoreboard.fromkeys(list(self.Main_server.client_nick.keys()), 0)

    def game_handle(self, word, player_sock):
        if len(self.Main_server.client_nick.values()) >= 2:
            if not self.check_word_correct(list_words[-1], word):
                self.sock.send(b"Wrong word")
            elif not self.non_replay(word):
                self.sock.send(b"Repeat word")
            else:
                list_words.append(word)
                q = {player_sock: scoreboard.get(player_sock) + 1}
                scoreboard.update(q)
                if scoreboard.get(player_sock) == self.max_score:
                    self.game_over()
                else:
                    self.Main_server.send_all_except(word, player_sock)
                    self.Main_server.send_all_except(self.Main_server.client_nick.get(player_sock) + ": + 1",
                                                     player_sock, server_message=True)

    def game_over(self):
        global game_bool
        win_score = max(list(scoreboard.values()))
        win_sock = self.get_value(scoreboard, win_score)
        game_bool = False
        self.Main_server.send_all_except("Game over!", except_client=win_sock, server_message=True)
        self.Main_server.send_all_except("Win "+self.Main_server.client_nick.get(win_sock) + "\n", server_message=True)
        self.Main_server.send_all_except("Type 'exit' to exit", server_message=True)

    def get_value(self, dic, value):
        for name in dic:
            if dic[name] == value:
                return name

    def check_word_correct(self, input_word, output_word):
        if input_word[-1:] == output_word[:1]:
            return True
        return False

    def non_replay(self, word):
        if word not in list_words:
            return True
        return False


class Chat_dispatcher(asyncore.dispatcher_with_send):
    _server = None

    def __init__(self, m_socket, m_server):
        asyncore.dispatcher_with_send.__init__(self, m_socket)
        self.sock = m_socket
        self._server = m_server
        self.start_chat(self.sock)

    def start_chat(self, sock_join):
        self.socket.send(b'You connect to Chat! Welcome!\n(For exit, input "exit")\n')

        self._server.send_all_except(
            '{} join to Chat'.format(self._server.client_nick.get(sock_join)),
            except_client=sock_join, server_message=True)

    def handle_read(self):
        data = self.recv(1024)
        data = data.decode("utf-8")
        if self._server.permit and data:
            self._server.send_all_except(data, except_client=self.sock)


class Server(asyncore.dispatcher):
    def __init__(self):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(('localhost', 5000))
        self.listen(2)
        self.client_nick = {}
        self.permit = False

    def handle_accept(self):
        sock, addr = self.accept()
        nick_thread = threading.Thread(target=self.create_nick(sock))
        nick_thread.start()
        nick_thread.join()
        Chat_dispatcher(sock, self)
        # Game_dispatcher(sock, self)

    def handle_close(self):
        self.close()

    def close(self):
        self.close()

    def exit_client(self, delete_client, delete_nick):
        self.send_all_except(str(delete_nick) + " disconnection", except_client=delete_client, server_message=True)
        # time.sleep(2)
        self.client_nick.pop(delete_client)

    def create_nick(self, sock_nick):
        sock_nick.send(b'Your Nickname: ')
        while True:
            sock_nick.setblocking(True)
            nick = sock_nick.recv(1024)
            nick = nick.decode("utf-8")
            if not nick:
                continue
            if nick in list(self.client_nick.values()):
                sock_nick.send(b'Think of a new nickname')
                continue
            else:
                self.client_nick.update({sock_nick: nick})
                break
        self.permit = True

    def send_all_except(self, data, except_client=None, server_message=False):
        if data:
            for sock_key, nick_value in zip(list(self.client_nick.keys()), list(self.client_nick.values())):
                if server_message:
                    message = "SERVER: " + data
                    sock_key.send(message.encode())
                else:
                    if sock_key is not except_client:
                        if data == "exit":
                            data = ""
                            self.exit_client(except_client, self.client_nick.get(except_client))
                            continue
                        message = self.client_nick.get(except_client) + ": " + data
                        sock_key.send(message.encode())


server = Server()
asyncore.loop()