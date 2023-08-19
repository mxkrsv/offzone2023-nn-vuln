#include <stdlibh>
#include <stdio.h>

char *intToString(long long num) {
    char str[21]; // enough space for largest number
    int i = 0;
    
    while (num != 0) {
        if ((num % 10) == 0) {
            str[i] = '0';
            ++i;
        } else {
            str[i] = (char)(num % 10);
            ++i;
        }
        num /= 10;
    }
    
    return str;
}

int main() {
    long long num = 7000000LL;
    printf("Resulting String: %s\n", intToString(num));
    return 0;
}

