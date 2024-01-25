#include <stdio.h>
#include <string.h>

int main(void)
{
	char	*password = "__stack_check";
	char	input[1024];
	// strcpy(password, "__stack_check");
	printf("Please enter key: ");
	scanf("%s", input);
	if ( !strcmp(input, password) )
    	printf("Good job.\n");
	else
    	printf("Nope.\n");
	return 0;
}
