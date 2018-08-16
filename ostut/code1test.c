#include<stdio.h>
#include<sys/stat.h>
#include<stdlib.h>
#include<fcntl.h>
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

int main(int argc, char const *argv[])
{

    int fd,dest;
    int n;

    int 

    fd = open("inputfile.txt",O_RDONLY,0400);
    dest = open("outfile.txt",O_CREAT|O_RDWR,0700);

    if (fd<0){
        perror("open inputfile err");
        exit(1);
    }



    for (int i=0;i<n;i++){
        //printf("%c %i ",a[i],i);
        printf("%c",a[i]);
    }

    for (int i=0;i<n;i++){
        a[i] = togglecase(a[i]);
    }

    for (int i=0;i<n;i++){
        //printf("%c %i ",a[i],i);
        printf("%c",a[i]);
    }

    printf("\n");

    return 0;
}
