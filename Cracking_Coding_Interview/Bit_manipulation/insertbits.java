// ben isenberg 9/25/2016
import java.util.*;

class Bits
{
	//insert m into n from bit i to bit j
	public static int insertBits(int n, int m, int i, int j)
	{
		//n = 512;  // 1000000000
		//m = 19;  //10011
		//i = 2;
		//j = 6;

		//shift m over by i bits
		m = m << i;

		//System.out.println(Integer.toBinaryString(m));

		//clear bits i thru j in n
		int length = j - i + 1;

		//make mask same length as n
		int num_bits = (int) Math.floor(Math.log(n) / Math.log(2)) + 1;

		//System.out.println(num_bits);

		int mask = 1;

		for (int x = 0; x < (num_bits - j); x++)
		{
			mask = mask << 1;
			mask = mask | 1;
		}

		mask = mask << length;

		for (int x = 0; x < i; x++)
		{
			mask = mask << 1;
			mask = mask | 1;
		}

		//System.out.println(Integer.toBinaryString(mask));
		//System.out.println("n = " + Integer.toBinaryString(n));

		n = n & mask; //clear bits in n

		//System.out.println(Integer.toBinaryString(n));		

		n = n | m;  // set bits to m

		System.out.println(Integer.toBinaryString(n));

		return 0;
	}


	public static void main(String[] args)
	{
		Bits.insertBits(1024,19,2,6);
		Bits.insertBits(1024,19,1,5);

		Bits.insertBits(1024,357,0,8);		
	}

}