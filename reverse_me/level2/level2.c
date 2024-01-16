#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int	no()
{
	puts("Nope.");
	exit(1);
}

int	ok()
{
	return puts("Good job.");
}

int	main(void)
{
	int				i;
	unsigned int	j;
	int				ret_scanf;
	bool			check_len = false;
	char			input[4096];
	char			new_str[9];
	char			arg_atoi[4];

	printf("Please enter key: ");
	ret_scanf = scanf("%23s", input);

	if ( ret_scanf != 1 )
    	no();
	if ( input[1] != '0' )
		no();
	if ( input[0] != '0' )
		no();

	fflush(stdin);
	memset(new_str, 0, 9);
	new_str[0] = 'd';
	arg_atoi[3] = '\0';
	j = 2;

	for (i = 1; ; ++i)
	{
		check_len = 0;
		if ( (unsigned int)strlen(new_str) < 8)
			check_len = j < strlen(input);
		if (!check_len)
			break;
		arg_atoi[0] = input[j];
   		arg_atoi[1] = input[j + 1];
    	arg_atoi[2] = input[j + 2];
		new_str[i] = atoi(arg_atoi);
		j += 3;
	}
	new_str[i] = '\0';
	if ( !strcmp(new_str, "delabere") )
    	ok();
	else
		no();
	return 0; 

}
