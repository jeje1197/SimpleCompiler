#include <stdio.h>
#include <string.h>

char* addStrings(char* str1, char* str2, char* dest) {
    strcat(dest, str1);
	strcat(dest, str2);
    return dest;
}

/* Compiled from SimpleC to C */
int main(int argc, char *argv[]) {
	char dest[80] = "";
	printf("%s\n", "pcsell");
    return 0;
}