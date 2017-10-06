CC=gcc
CFLAGS=-I.

ODIR=obj_dir
LIBS=-lm
DEPS=dc.h dp.h
_OBJ=run_experiments.o dc.o
OBJ=$(patsubst %,$(ODIR)/%,$(_OBJ))

$(ODIR)/%.o: %.c $(DEPs)
	$(CC) -c -o $@ $< $(CFLAGS)

run_experiments: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o
