#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* intToStringWithCommas(int num) {
    char temp[20];  // Assuming the integer won't be larger than 20 digits
    sprintf(temp, "%d", num);
    
    int len = strlen(temp);
    int commaCount = (len - 1) / 3;
    int newLen = len + commaCount;
    
    char* result = (char*)malloc(newLen + 1);
    if (!result) {
        return NULL; // Memory allocation failed
    }
    
    int index = newLen - 1;
    int tempIndex = len - 1;
    int commaCounter = 0;
    
    while (tempIndex >= 0) {
        if (commaCounter == 3) {
            result[index--] = ',';
            commaCounter = 0;
        } else {
            result[index--] = temp[tempIndex--];
            commaCounter++;
        }
    }
    
    result[newLen] = '\0';
    return result;
}

int main() {
    int num = 7000000;
    char* str = intToStringWithCommas(num);
    
    if (str) {
        printf("%s\n", str);
        free(str); // Don't forget to free the allocated memory
    } else {
        printf("Memory allocation failed.\n");
    }
    
    return 0;
}
