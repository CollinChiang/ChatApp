LOG_FP = "logs.txt"


class FileWrite:
    def clear():
        file = open(LOG_FP, "w")
        file.close()

    def write(value: str):
        file = open(LOG_FP, "a")
        file.write(f"{value}\n")
        file.close()
