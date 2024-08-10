import random
import logging

logging.basicConfig(level=logging.DEBUG)


class Interpreter:

    def __init__(self, filePath: str):
        self.path = filePath

        if not filePath.endswith(".bad"):
            logging.error("[ERROR 1] Invalid file type.")
            return

        self.rows: list[list[str]] = []

    def run(self):
        with open(self.path, "r") as f:
            for row in f.readlines(-1):
                self.rows.append(row.strip().split())

        sayTimes = 0

        for row in self.rows:
            cmd = row.pop(0)

            if cmd == "Say":
                if sayTimes < 3:
                    logging.info("SayError: Why should I?")
                elif sayTimes > 8:
                    logging.info("SayError: Ap ap ap, you did  it too much!")
                else:
                    logging.info(" ".join(["Okay fine:", *[w for w in row]]))

                sayTimes += 1


if __name__ == "__main__":
    interprter = Interpreter("test_say.bad")
    interprter.run()
