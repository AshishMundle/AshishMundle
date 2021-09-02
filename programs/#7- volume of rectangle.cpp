// volume of rectangle //

#include <stdio.h>
int main ()
{
	float l,w,h,v;
	printf ("\n enter the value of l:- ");
	scanf ("%f",&l);
	printf("\n enter the value of w:- ");
	scanf ("%f",&w);
	printf ("\n enter the value of h :-");
	scanf ("%f",&h);
	v=l*w*h;
	printf ("\n volume of rectangle is %.2f",v);
	return 0;
}
