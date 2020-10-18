import random
import select
import socket
import sys

TIMEOUT = 60
NUM_GUESSES = 5
LOWER_LIMIT = 1
UPPER_LIMIT = 32

def play_guessing_game(client):
    guessesUsed = 0
    random_number = get_random_number()

    name = prompt_user(client, "Hello! What is your name?\n")
    if not name:
        print("No valid name was given. Closing connection.")
        return

    greet_player(client, name)
    
    for guesses_used in range(1, NUM_GUESSES + 1):
        guess = prompt_for_guess(client)

        if guess < random_number:
            client.sendall(bytes("Too low, try again.\n", "ascii"))
        if guess > random_number:
            client.sendall(bytes("Too high, try again.\n", "ascii"))
        if guess == random_number:
            break

    if guess == random_number:
        client.sendall(bytes(f"Well done, {name}! You guessed correctly in {guesses_used} guesses.", "ascii"))
    else:
        client.sendall(bytes(f"Sorry, out of guesses. The number I'm thinking of is {random_number}.", "ascii"))

def get_random_number():
    random_number = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    print(f"Secret number is {random_number}")

    return random_number

def prompt_user(client, msg):
    try:
        response = ""
        client.sendall(bytes(msg, "ascii"))
        while not response or '\n' != response[-1]:
            ready = select.select([client], [], [], TIMEOUT)
            if not ready[0]:
                raise socket.timeout

            response_byte = client.recv(1)
            response += str(response_byte, "ascii")

        return response.strip()
    except UnicodeDecodeError:
        client.sendall(b"Error: This game only accepts ascii characters.")
        return None

def greet_player(client, name):
    client.sendall(bytes(f"Greetings, {name}, I'm thinking of a number between {LOWER_LIMIT} and {UPPER_LIMIT}.\n", "ascii"))
    client.sendall(bytes(f"You get {NUM_GUESSES} guesses.\n", "ascii"))

def prompt_for_guess(client):
    guess = prompt_user(client, "Make a guess:\n")

    while not guess:
        guess = prompt_user(client, "Error! You must make a guess: \n")
    
    return int(guess)


def main():
    host = "0.0.0.0"
    port = int(sys.argv[1])

    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        s.bind((host, port))

        s.listen()
        while True:
            client, addr = s.accept()
            client.setblocking(True)

            try:
                play_guessing_game(client)
            except socket.timeout:
                print("Client timed out.")
            except BrokenPipeError:
                print("Connection closed unexpectedly.")
            finally:
                if client.fileno != -1:
                    client.close()

if __name__ == "__main__":
    main()
