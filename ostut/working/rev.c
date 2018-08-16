#include<stdlib.h>
#include<stdio.h>
#include<fcntl.h>
#include<sys/stat.h>
#include<unistd.h>

char togglecase(char c){
    /*
     * Function to toggle case of an alphabet.
     */
    if (c >= 'A' && c <= 'Z'){
        c = (char)(32 + (int)c);
    }
    else if (c >= 'a' && c <= 'z'){
        c = (char)((int)c - 32);
    }
    return c;
}


int main(int argc, char *argv[]) {

    int infile, outfile, n;
    char storage;
    long long int filesize;
    long long int i;

    if (argc != 3) {
        printf("usage %s <infile> <outfile>", argv[0]);
        exit(1);
    }
    
    infile = open(argv[1], O_RDONLY, 0400);
    outfile = open(argv[2], O_RDWR|O_CREAT, 0600);

    if (infile < 0) {
        write(STDERR_FILENO,"can't open infile",20);
        exit(1);
    }

    if (outfile < 0) {
        write(STDERR_FILENO,"can't create outfile",22);
        exit(1);
    }

    filesize = lseek(infile, (off_t) 0, SEEK_END);

    i = filesize - 1;

    while (i>=0) {
        lseek(infile, (off_t) i, SEEK_SET);

        n = read(infile, &storage, 1);

        if (n < 0) {
            write(STDERR_FILENO,"can't read 1 byte",20);
            exit(1);
        }

        //printf("%c",storage);
        storage = togglecase(storage);

        n = write(outfile, &storage, 1);
        if (n < 0) {
            write(STDERR_FILENO,"can't write 1 byte",20);
            exit(1);
        }

        i++;

    }
    close(infile);
    close(outfile);

    return 0;
}