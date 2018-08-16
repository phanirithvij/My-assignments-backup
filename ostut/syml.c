#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int s;

    s = symlink("linux_systemcall_reference.pdf","linux.pdf");

    return 0;
}