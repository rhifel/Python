import sys
#import pyparsing
#import lark
# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    print(f"Input: {input_line} | Pattern: {pattern}")  # Debugging line
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern == "\\d":
        return any(c.isdigit() for c in input_line)
    elif pattern == "\\w":
        return any(c.isalnum() or c == '_' for c in input_line)
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
         exit(0)
    else:
         exit(1)


if __name__ == "__main__":
    main()