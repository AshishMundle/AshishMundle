	//percentage maker//

#include<stdio.h>
int main ()
{
	float mat,sci,eng,total,perc;
	printf("enter marks of mat:");
	scanf("%f",&mat);
	printf("enter marks of sci:");
	scanf("%f",&sci);
	printf("enter marks of eng:");
	scanf("%f",&eng);
	total=mat+sci+eng;
	printf("marks is %.2f",total);
	perc=total/300*100;
	printf("\nyou get %0.2f percentage ",perc);
	return 0;
}
