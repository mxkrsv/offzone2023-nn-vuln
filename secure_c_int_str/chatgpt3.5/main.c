#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* secureIntToStringWithCommas(int num) {
    // Allocate memory for the result string
    char* result = (char*)malloc(20); // Longest int + commas + negative sign + null terminator
    if (result == NULL) {
        // Handle memory allocation error
        return NULL;
    }

    // Handle negative numbers
    if (num < 0) {
        num = -num;
        strcpy(result, "-");
    } else {
        result[0] = '\0';
    }

    char temp[20]; // Temporarily store each section of the number
    int count = 0; // Count the number of digits

    do {
        sprintf(temp, "%d", num % 1000); // Get the last three digits
        if (num >= 1000) {
            // Add comma separator
            memmove(temp + 4, temp, strlen(temp) + 1); // Make space for comma
            temp[1] = ',';
        }
        strcat(result, temp); // Add the section to the result
        num /= 1000; // Move to the next section
        count++;
    } while (num > 0);

    // Reverse the result string to get the correct order
    int len = strlen(result);
    for (int i = 0; i < len / 2; i++) {
        char temp = result[i];
        result[i] = result[len - i - 1];
        result[len - i - 1] = temp;
    }

    return result;
}

int main() {
    int num = 7000000;
    char* result = secureIntToStringWithCommas(num);

    if (result != NULL) {
        printf("Integer: %d\n", num);
        printf("String with commas: %s\n", result);
        free(result); // Remember to free the allocated memory
    } else {
        printf("Memory allocation error\n");
    }

    return 0;
}
