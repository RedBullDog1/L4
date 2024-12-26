import threading
import socket
def test_client(host, port, message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            client_socket.sendall(message.encode('utf-8'))
            data = client_socket.recv(1024)
            print(f"Response from server: {data.decode('utf-8')}")
    except ConnectionRefusedError:
        print("Failed to connect to the server.")
def main():
    host, port = '127.0.0.1', 11111
    threads = []
    for i in range(5):
        message = f"Epye, it works, response client {i + 1}"
        thread = threading.Thread(target=test_client, args=(host, port, message))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
if __name__ == "__main__":
    main()