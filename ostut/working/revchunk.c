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
    int chunk = 25200;
    char storage[chunk], reverse[chunk];
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


    long long int loopcount = filesize / chunk;
    int remainingbytes = filesize % chunk;

    printf("file : %lld\n", filesize);
    printf("loops : %lld\n", loopcount);
    printf("remaining bytes %d\n", remainingbytes);

    lseek(infile, (off_t) (filesize - remainingbytes), SEEK_SET);

    n = read(infile, storage, remainingbytes);

    if (n < 0) {
        write(STDERR_FILENO,"can't read bytes",20);
        exit(1);
    }

    //printf("%c",storage);
    for(int j=0;j<remainingbytes;j++){
        storage[j] = togglecase(storage[j]);
        reverse[remainingbytes-j-1] = storage[j];
    }

    //for (int j=0;j<remainingbytes;j++){
      //  printf("%c ",reverse[j]);
    //}

    n = write(outfile, reverse, remainingbytes);
    if (n < 0) {
        write(STDERR_FILENO,"can't write bytes",20);
        exit(1);
    }

    i = 0;

    while (i<loopcount) {
        lseek(infile, (off_t) ((loopcount -i - 1)*chunk), SEEK_SET);

        n = read(infile, storage, chunk);

        //printf("%c",storage);
        for(int j=0;j<chunk;j++){
            storage[j] = togglecase(storage[j]);
            reverse[chunk-j-1] = storage[j];
        }

        n = write(outfile, reverse, chunk);

        i++;

        if (n < 0) {
            write(STDERR_FILENO,"can't write bytes",20);
            exit(1);
        }
        if (n < 0) {
            write(STDERR_FILENO,"can't read bytes",20);
            exit(1);
        }
    }
    

    close(infile);
    close(outfile);

    return 0;
}