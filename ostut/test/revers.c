#include<stdio.h>

int main(int argc, char const *argv[])
{
    int remainingbytes = 20;
    int storage[remainingbytes], storage2[remainingbytes];

    for (int j=0;j<remainingbytes;j++){
        storage[j] = j*2;
    }
    
    for(int j=0;j<remainingbytes;j++){
        storage2[j] = storage[remainingbytes-j-1];
    }

    for (int j=0;j<remainingbytes;j++){
        printf("%d ",storage2[j]);
    }

    return 0;
}