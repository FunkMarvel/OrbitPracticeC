CC := gcc
PCC := mpicc
FLAGS = -Wall -O3

.PHONY : all clean

all: main.exe

main.exe: main.o integrate.o extrafunc.o
	$(CC) main.o integrate.o extrafunc.o -o main.exe

main.o: main.c
	$(CC) $(FLAGS) main.c -c

integrate.o: integrate.c
	$(CC) $(FLAGS) integrate.c -c

extrafunc.o: extrafunc.c
	$(CC) $(FLAGS) extrafunc.c -c

clean :
	rm -f *.o
	rm -f *.exe

print-%  : ; @echo $* = $($*)
