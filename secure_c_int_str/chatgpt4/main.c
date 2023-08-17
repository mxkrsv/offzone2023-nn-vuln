#include <stdio.h>
#include <stdlib.h>

char* intToStrWithCommas(int num) {
    // Allocate maximum possible space: -2,147,483,648 has 13 characters including commas and negative sign
    char* buffer = (char*)malloc(14 * sizeof(char));
    if (buffer == NULL) {
        perror("Failed to allocate memory");
        exit(EXIT_FAILURE);
    }
    
    int isNegative = 0;
    if (num < 0) {
        isNegative = 1;
        num = -num;  // convert to positive for processing
    }
    
    int idx = 13;
    buffer[idx] = '\0'; // Null terminate the string
    idx--;

    int commaCounter = 0;
    
    do {
        buffer[idx] = '0' + (num % 10);
        num /= 10;
        idx--;
        commaCounter++;
        
        if (commaCounter == 3 && num != 0) {
            buffer[idx] = ',';
            idx--;
            commaCounter = 0;
        }
        
    } while (num != 0);

    if (isNegative) {
        buffer[idx] = '-';
    } else {
        idx++;
    }

    // Compact the string
    char* result = strdup(&buffer[idx]);
    free(buffer);
    if (result == NULL) {
        perror("Failed to duplicate string");
        exit(EXIT_FAILURE);
    }
    
    return result;
}

int main() {
    int test = 7000000;
    char* result = intToStrWithCommas(test);
    printf("%s\n", result);
    free(result);

    return 0;
}
