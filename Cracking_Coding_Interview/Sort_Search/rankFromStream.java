// ben isenberg 10/22/2016
import java.util.*;

//Sorted linked list class
class SortedNode 
{
	SortedNode next = null;
	int data;

	public SortedNode(int d)
	{
		data = d;
	}

	void insertNode(SortedNode x)
	{
		SortedNode n = this;
		SortedNode prev = this;

		if (this.length() < 2)
		{
			if (n.data > x.data)
			{
				int temp = n.data;
				n.data = x.data;
				x.data = temp;
			}
			n.next = x;
			return;
		}

		while (n != null && n.data <= x.data)
		{
			prev = n;
			n = n.next;
		}
		prev.next = x;
		x.next = n;	
	}

	void print()
	{
		SortedNode n = this;
		while (n != null)
		{
			System.out.println(n.data);
			n = n.next;
		}
			System.out.println();
	}

	int length()
	{
		int len = 0;

		SortedNode n = this;

		while (n != null)
		{
			len = len + 1;
			n = n.next;
		}

		return len;
	}

	int getRankOfNumber(int x)
	{
		int rank = 0;

		SortedNode n = this;

		while (n.next != null && n.data <= x)
		{
			rank += 1;
			n = n.next;
		}

		return rank - 1;
	}

	public static void main(String[] args)
	{
		SortedNode test = new SortedNode(5);
		test.insertNode(new SortedNode(1));
		test.insertNode(new SortedNode(4));
		test.insertNode(new SortedNode(4));
		test.insertNode(new SortedNode(5));
		test.insertNode(new SortedNode(9));
		test.insertNode(new SortedNode(7));
		test.insertNode(new SortedNode(13));
		test.insertNode(new SortedNode(3));

		test.print();

		System.out.println(test.getRankOfNumber(1));
		System.out.println(test.getRankOfNumber(3));
		System.out.println(test.getRankOfNumber(4));
	}
}