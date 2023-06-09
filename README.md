# makemake

`makemake` is a simple Makefile generator for C projects.

## Example

Example input file `Makefile.in`:

```makefile
PROG=prog      # the program name
DIR=src/       # the source code directory
STD=c99        # the C standard
BUILD=build/   # the output directory
```

Assume we have the following project files:

```
src/config.h
src/lex.h
src/lex.c
src/main.c
```

Then the output `Makefile` is as follows:

```makefile
# Makefile generated by makemake - by Andreas Schwenk
PROG=prog
CC=gcc -std=c99
BUILD_DIR=build/
INC=
LIB=
CFLAGS=$(FLAGS)
HEADERS=src/config.h src/lex.h
OBJS=$(BUILD_DIR)lex.o $(BUILD_DIR)main.o

$(shell mkdir -p $(BUILD_DIR))

all: $(PROG)
clean:
	rm -rf $(BUILD_DIR)

$(PROG): $(OBJS)
	$(CC) $(OBJS) $(INC) $(CFLAGS) $(LIB) -o $(BUILD_DIR)$(PROG)
$(BUILD_DIR)lex.o: src/lex.c $(HEADERS)
	$(CC) src/lex.c $(INC) $(CFLAGS) -c -o $(BUILD_DIR)lex.o
$(BUILD_DIR)main.o: src/main.c $(HEADERS)
	$(CC) src/main.c $(INC) $(CFLAGS) -c -o $(BUILD_DIR)main.o
```

## Usage

### Installation

```bash
pip install makemake
```

### Command Line

```bash
makemake 'Makefile.in'
```

### API

```python
import makemake

# creates output 'Makefile' using meta data specified
# in 'Makefile.in'
makemake.makemake('Makefile.in', 'Makefile')
```
