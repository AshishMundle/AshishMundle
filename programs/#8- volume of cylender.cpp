// volume of cylender //

#include <stdio.h>
int main ()
{
	float pi,r,h,v;
	printf("\n enter the value of pi:");
	scanf("%f",&pi);
	printf("\n enter the value of r:");
	scanf("%f",&r);
	printf("\n enter the value of h:");
	scanf("%f",&h);
	v=pi*r*r*h;
	printf("\n volume of cylender is %.2f",v);
	return 0 ; 
}
