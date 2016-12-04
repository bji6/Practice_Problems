//Ben isenberg 10/22/2016
#include <iostream>
#include <stdlib.h>
using namespace std;


//reverse a null terminated string
void reverse(char * str)
{
	//find length of string
	int length = 0;
	char* temp = str;
	while (*temp != NULL)
	{
		temp++;
		length++;
	}

	char array[length];
	//cout << length << endl;

	temp = str;
	int x = 0;
	//store characters in an array
	while (*temp != NULL)
	{
		array[x] = *temp;
		//cout << array[x] << endl;
		temp++;
		x++;
	}

	//cout << x << endl;

	//reverse characters
	temp = str;
	while (x > 0)
	{
		*temp = array[x-1];
		temp++;
		x--;
	}

	//print results
	temp = str;
	while (*temp != NULL)
	{
		cout << *temp;
		temp++;
	}

	cout << endl;

	return;
}



int main(int argc, char* argv[])
{
	char test[] = "RedRum";
	
	char *ptr = test;

	reverse(ptr);
	return 0;
}