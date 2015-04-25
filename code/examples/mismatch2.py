def bomb() -> str:
    return "☠"

def num() -> int:
    return 3

def main():
    num() + bomb()

def other():
    num(bomb())


main()
