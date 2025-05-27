from speech_handler import get_command

cmd = get_command()
if cmd:
    print(f"Command received: {cmd}")
else:
    print("No command received.")