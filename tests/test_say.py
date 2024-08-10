from pathlib import Path
from unittest.mock import patch, call
from Interpreter import Interpreter


def test_say_command():
    filePath = str(Path(__file__).parent.parent / "test_say.bad")
    inter = Interpreter(filePath)

    with patch("logging.info") as mock_info:
        inter.run()

        assert mock_info.mock_calls == [
            call("SayError: Why should I?"),
            call("SayError: Why should I?"),
            call("SayError: Why should I?"),
            call("Okay fine: Hello"),
            call("Okay fine: Hi, how are you"),
            call("Okay fine: something"),
            call("Okay fine: something"),
            call("Okay fine: something"),
            call("Okay fine: something"),
            call("SayError: Ap ap ap, you did  it too much!"),
            call("SayError: Ap ap ap, you did  it too much!"),
        ]
