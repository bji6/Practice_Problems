// ben isenberg 9/25/2016
import java.util.*;

class Bits
{
	//swap all even and odd bits in binary number n
	public static int pairwiseSwap(int n)
	{
		int even_mask = 0x55555555; //0101

		int odd_mask = 0xAAAAAAAA;  //1010

		//shift even bits left by 1
		int even_bits = n & even_mask;
		even_bits = even_bits << 1;

		//shift odd bits right by 1
		int odd_bits = n & odd_mask;
		odd_bits = odd_bits >> 1;

		int result = even_bits | odd_bits;

		return result;
	}


	public static void main(String[] args)
	{
		System.out.println(Integer.toBinaryString(Bits.pairwiseSwap(53)));

		System.out.println(Integer.toBinaryString(Bits.pairwiseSwap(13)));

		System.out.println(Integer.toBinaryString(Bits.pairwiseSwap(27)));		
	}

}