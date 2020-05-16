CC := gcc
PCC := mpicc
FLAGS = -Wall -O3

.PHONY : all clean

all: main.exe

main.exe: main.o integrate.o extrafunc.o writefile.o
	$(CC) main.o integrate.o extrafunc.o writefile.o -o main.exe -lm

main.o: main.c
	$(CC) $(FLAGS) main.c -c

integrate.o: integrate.c
	$(CC) $(FLAGS) integrate.c -c

extrafunc.o: extrafunc.c
	$(CC) $(FLAGS) extrafunc.c -c

writefile.o: writefile.c
	$(CC) $(FLAGS) writefile.c -c

clean :
	rm -f *.o
	rm -f *.exe
	rm -f *.bin

print-%  : ; @echo $* = $($*)
