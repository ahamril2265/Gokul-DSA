class TextEditor:
    """A simple text editor with an undo feature using a stack.

    Supported operations:
    - append(text): add text to the end
    - delete(k): remove last k characters
    - undo(): revert the most recent operation
    - get_text(): current text
    """

    def __init__(self):
        self._text = ""
        self._undo_stack = []  # stack of inverse operations

    def append(self, s: str) -> None:
        if not s:
            return
        self._text += s
        # inverse: delete last len(s) chars
        self._undo_stack.append(("delete", len(s)))

    def delete(self, k: int) -> str:
        if k <= 0:
            return ""
        k = min(k, len(self._text))
        deleted = self._text[-k:]
        self._text = self._text[:-k]
        # inverse: insert the deleted text back
        self._undo_stack.append(("insert", deleted))
        return deleted

    def undo(self) -> bool:
        if not self._undo_stack:
            return False
        op = self._undo_stack.pop()
        if op[0] == "delete":
            n = op[1]
            # remove last n chars (if present)
            n = min(n, len(self._text))
            self._text = self._text[:-n]
        elif op[0] == "insert":
            s = op[1]
            self._text += s
        else:
            # unknown op, ignore
            return False
        return True

    def get_text(self) -> str:
        return self._text


if __name__ == "__main__":
    # small interactive demo
    editor = TextEditor()
    print("Simple TextEditor demo. Commands: a <text>, d <n>, u, q")
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break
        if not line:
            continue
        if line == "q":
            break
        if line == "u":
            ok = editor.undo()
            print("undo:", ok, "->", editor.get_text())
            continue
        if line.startswith("a "):
            editor.append(line[2:])
            print(editor.get_text())
            continue
        if line.startswith("d "):
            try:
                n = int(line[2:])
            except ValueError:
                print("invalid number")
                continue
            editor.delete(n)
            print(editor.get_text())
            continue
        print("unknown command")
