#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int s;
    int fd;

    fd = open("test", O_RDWR|O_CREAT, 600);

    s = symlinkat("rev.c",fd,"revlink.c");

    return 0;
}