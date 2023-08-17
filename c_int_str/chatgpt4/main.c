#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* intToStringWithCommas(int num) {
    char buffer[20]; // Assuming 32-bit int
    char *result;
    int i = 0, j = 0, count = 0;

    // Check if the number is negative
    int isNegative = 0;
    if (num < 0) {
        isNegative = 1;
        num = -num;
    }

    // Convert the integer to string without commas
    sprintf(buffer, "%d", num);

    // Calculate the length of the string needed
    int len = strlen(buffer);
    int commas = (len - 1) / 3;
    int resultLen = len + commas;

    if (isNegative) {
        resultLen++;  // For the negative sign
    }

    result = (char*)malloc(resultLen + 1); // +1 for the null terminator
    if (!result) {
        return NULL;  // Memory allocation failure
    }

    if (isNegative) {
        result[j++] = '-';
    }

    while (buffer[i]) {
        result[j++] = buffer[i++];
        if ((len - i) % 3 == 0 && buffer[i]) {
            result[j++] = ',';
        }
    }
    result[j] = '\0';  // Null-terminate the string

    return result;
}

int main() {
    int num = 7000000;
    char *str = intToStringWithCommas(num);
    if (str) {
        printf("%d -> %s\n", num, str);
        free(str);  // Free the allocated memory
    }
    return 0;
}
