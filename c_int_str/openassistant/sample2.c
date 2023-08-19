#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* string_num(int num) {
    char str[256]; // assuming max size of int is 2^18-1
    sprintf(str, "%d,%03d", num / 1000, num % 100);
    return str;
}
