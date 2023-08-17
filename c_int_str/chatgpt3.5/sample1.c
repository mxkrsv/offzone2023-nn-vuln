#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* formatInteger(int num) {
    // Convert the integer to a string
    char numStr[20]; // Adjust the array size as needed
    sprintf(numStr, "%d", num);

    int len = strlen(numStr);
    int commaCount = (len - 1) / 3; // Calculate how many commas are needed
    int newLen = len + commaCount;

    // Allocate memory for the formatted string
    char* formatted = (char*)malloc(newLen + 1); // +1 for the null terminator
    int j = newLen - 1;

    // Loop through the original string in reverse and add commas
    for (int i = len - 1; i >= 0; i--) {
        formatted[j--] = numStr[i];
        if ((len - i) % 3 == 0 && i != 0) {
            formatted[j--] = ',';
        }
    }

    formatted[newLen] = '\0'; // Null-terminate the formatted string
    return formatted;
}

int main() {
    int num = 7000000;
    char* formattedNum = formatInteger(num);
    printf("Formatted number: %s\n", formattedNum);
    free(formattedNum); // Remember to free the allocated memory
    return 0;
}
