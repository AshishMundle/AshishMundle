// checking weekend days or working days 

#include <stdio.h>
#include <string.h>
int main ()
{
	char day [4];
	printf("enter any day:");
	gets (day);
	if (strcmp(day,"saturday")==0||strcmp(day,"sunday")==0)
	printf("weekend");
	else
	printf("working day");
	return 0;
}
