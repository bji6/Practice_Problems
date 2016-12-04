//ben isenberg 9/10/2016

#include <iostream>
#include <typeinfo>
using namespace std;

void char_replace(char* string1, int size)
{
	char space = ' ';
	int number_of_spaces = 0;
	int array_size = size;

	char* ptr = string1;

	//count number of spaces in string
	for(int i = 0; i < size; i++)
	{
		//cout << typeid(*ptr).name() << "\n";

		if ((*ptr) == space)
		{
			number_of_spaces++;
		}
		
		ptr++;
	}

	if (number_of_spaces == 0)
	{
		number_of_spaces = 1;
	}

	int new_size = (number_of_spaces*2) + array_size + 1;

	char my_str[new_size];

	ptr = string1;

	int x = 0;

	//cout << number_of_spaces << "\n";

	while (x < (new_size - 1))
	{
		if (*ptr == space)
		{
			my_str[x] = '%';
			x++;
			my_str[x] = '2';
			x++;
			my_str[x] = '0';
			x++;
			ptr++;
			continue;
		}

		my_str[x] = *ptr;
		x++;
		ptr++;
	}

	my_str[x] = '\0';

	cout << my_str << "\n";
	
	return;
}



int main()
{
	char test[] = "Mr John Smith    ";
	
	char *ptr = test;

	cout << test << "\n";

	char_replace(ptr, 13);

	return 0;
}