#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int		___syscall_malloc()
{
	return puts("Good job.");
}

void	__syscall_malloc()
{
	puts("Nope.");
	exit(1);
}

int		main(void)
{
	int				i;
	unsigned int	j;
	int				ret_scanf;
	int				ret_strcmp;
	bool			check_len = false;
	char			input[4096];
	char			new_str[9];
	char			arg_atoi[4];

	printf("Please enter key: ");
	ret_scanf = scanf("%23s", input);

	if ( ret_scanf != 1 )
		__syscall_malloc();
	if ( input[1] != '2' )
		__syscall_malloc();
	if ( input[0] != '4' )
		__syscall_malloc();

	fflush(stdin);
	memset(new_str, 0, sizeof(new_str));
	new_str[0] = '*';
	arg_atoi[3] = '\0';
	j = 2;

	for (i = 1; ; ++i)
	{
		check_len = false;
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
	ret_strcmp = strcmp(new_str, "********");
	if ( ret_strcmp == -2 )
	__syscall_malloc();
	if ( ret_strcmp == -1 )
	__syscall_malloc();
	if ( ret_strcmp )
	{
		if ( ret_strcmp != 1 )
		{
			if ( ret_strcmp != 2 )
			{
				if ( ret_strcmp != 3 )
				{
				if ( ret_strcmp != 4 )
				{
					if ( ret_strcmp != 5 )
					{
					if ( ret_strcmp != 115 )
						__syscall_malloc();
					__syscall_malloc();
					}
					__syscall_malloc();
				}
				__syscall_malloc();
				}
				__syscall_malloc();
			}
			__syscall_malloc();
		}
		__syscall_malloc();
	}
	___syscall_malloc();
	return 0; 

}
	