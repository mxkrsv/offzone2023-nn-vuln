#include <stdlib.h>
#include <stdio.h>
#include <limits.h>

char *int_to_string(signed int num) {
    char str[21]; // enough space for largest number
    int pos = 0;
    
    if (num == INT_MIN) {
        sprintf(&str[pos], "-%d", -1);
        return &str[pos];
    }

    char temp[64] = { 0 };
    int length = snprintf(temp, sizeof(temp), "%lld");
    memcpy(&str[pos + 1], temp, min(length, 20));

    return &str[pos];
}

void printNumberAsString() {
    int num = atoi(int_to_string(&num));
    printf("Input: %s\n", int_to_string(&num));
}

int main() {
    int num = 7000000;
    printNumberAsString();
    return 0;
}
