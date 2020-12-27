# Advent of Code 2020

## Day 3

### Task 1

```bash
./task1.awk -v h=3 -v v=1 < input.txt
178
```

### Task 2

```bash
(./task1.awk -v h=1 -v v=1 < input.txt
./task1.awk -v h=3 -v v=1 < input.txt
./task1.awk -v h=5 -v v=1 < input.txt
./task1.awk -v h=7 -v v=1 < input.txt
./task1.awk -v h=1 -v v=2 < input.txt
) | awk 'BEGIN{s=1} NF {s*=$1} END {printf "%.0f", s}'
3492520200
```

