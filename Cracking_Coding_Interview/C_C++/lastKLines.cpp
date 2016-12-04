//Ben isenberg 10/22/2016
#include <fstream>
#include <iostream>
#include <stdlib.h>
using namespace std;


//read the last K lines of a file
int main(int argc, char* argv[])
{
	char k = *(argv[1]); 
	int num = k - '0';	//convert char to int

	//cout << num << endl;

	ifstream is("test.txt");

	// get length of file:
    int length = 0;
    string line;
    while (getline(is, line))
	{
		length++;
	}

	is.clear(); //clear eof flag
    is.seekg(0, is.beg); //move cusor to start of file

	//read thru file, print last K lines
	int lineNumber = 0;
	int offset = length - num;
	
	//cout << offset << endl;
	
	while (getline(is, line))
	{
		if (lineNumber >= offset)
		{
			cout << line << endl;
		}

		lineNumber++;
	}

	return 0;
}