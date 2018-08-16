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
    int no = 127;
    char a[no];

    for (int i=0;i<no;i++){
        a[i] = (char)i;
    }

    for (int i=0;i<no;i++){
        //printf("%c %i ",a[i],i);
        printf("%c",a[i]);
    }

    for (int i=0;i<no;i++){
        a[i] = togglecase(a[i]);
    }

    for (int i=0;i<no;i++){
        //printf("%c %i ",a[i],i);
        printf("%c",a[i]);
    }

    printf("\n");

    return 0;
}
