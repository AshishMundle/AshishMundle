// convertion of bytes in bits,kb,mb,gb,tb//

#include<stdio.h>
int main ()
{
	float bytes,bits,kb,mb,gb,tb;
	printf ("\n enter the number of bytes :");
	scanf ("%f",&bytes);
	bits=bytes*8;
	kb=bits/1024;
	mb=kb/1024;
	gb=mb/1024;
	tb=gb/1024;
	printf("\n=%.2f bits",bits);
	printf("\n=%.2f kb",kb);
	printf("\n=%.2f mb",mb);
	printf("\n=%.2f gb",gb);
	printf("\n=%.2f tb",tb);
	return 0 ;
}
