Cpp= g++


Target: $(kata).o
	$(Cpp) $(kata).o -o $(kata)-ggdb 

$(kata).o:  $(kata).cpp
	$(Cpp)  -c $(kata).cpp -ggdb

clean:
	rm *.o $(kata)
cleanall:
	rm *.o; ls | grep -v "\." | grep -v makefile | xargs rm
