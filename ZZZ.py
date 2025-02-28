#!/usr/bin/env python3

import sys


def main():
  top_words = []
  counts = {}
  paragraph_started = False
  paragraph_count = 0

  args = sys.argv[1:]
  pass_num = 0
  file_to_process = None

  for i, arg in enumerate(args):
    if arg.startswith("PASS="):
      pass_num = int(arg.split("=")[1])
      if i + 1 < len(args) and not args[i + 1].startswith("PASS="):
        file_to_process = args[i + 1]

        if pass_num == 1:
          with open(file_to_process, "r") as f:
            for line in f:
              word = line.strip()
              if word:
                top_words.append(word)
                counts[word] = 0

        elif pass_num == 2:
          print(",".join(top_words))

          with open(file_to_process, "r") as f:
            for line in f:
              line = line.strip()

              if not line:
                if paragraph_started:
                  print(",".join(str(counts[word]) for word in top_words))
                  for word in counts:
                    counts[word] = 0
                paragraph_started = False
              else:
                if not paragraph_started:
                  paragraph_started = True
                  paragraph_count += 1

                words = line.split()
                for word in words:
                  if word in counts:
                    counts[word] += 1

          if paragraph_started:
            print(",".join(str(counts[word]) for word in top_words))


if __name__ == "__main__":
  main()
