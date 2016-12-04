// ben isenberg 9/25/2016
import java.util.*;

class Bits
{
	//determine number of bits we need to flip to turn m into n
	public static int conversion(int n, int m)
	{
		int andd = n ^ m;

		System.out.println(Integer.toBinaryString(n));
		System.out.println(Integer.toBinaryString(m));
		System.out.println(Integer.toBinaryString(andd));

		//find number of bits of larger number
		int num_bits = (int) Math.floor(Math.log(n) / Math.log(2)) + 1;

		if (m > n)
		{
			num_bits = (int) Math.floor(Math.log(m) / Math.log(2)) + 1;			
		}

		int count = 0;

		//count nmumber of zeros, this is number of bits that need to be flipped
		for (int x = 0; x < num_bits; x++)
		{
			if ((andd & 1) == 1) //this is a bit we need to flip
			{
				count += 1;
			}

			andd = andd >> 1;
		}

		return count;
	}


	public static void main(String[] args)
	{
		System.out.println(Bits.conversion(29,15));

		System.out.println(Bits.conversion(32,12));	
	}

}