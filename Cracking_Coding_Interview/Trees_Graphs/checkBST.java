// ben isenberg 9/24/2016
import java.util.*;

class Node
{
	public Node left_child;
	public Node right_child;
	public int data;

	public Node(int n)
	{
		data = n;
	}

	public void setLeftNode(Node x)
	{
		left_child = x;
	}

	public void setRightNode(Node x)
	{
		right_child = x;
	}

	public Node getLeftNode()
	{
		return left_child;
	}

	public Node getRightNode()
	{
		return right_child;
	}

	//recursive function to check if a binary tree is binary search tree
	public static boolean checkBST(Node a, int min, int max)
	{
		//base case
		if (a == null)
		{
			return true;
		}

		boolean check = false;

		if (a.data >= min && a.data < max)
		{
			check = true;
		}

		boolean checkL = checkBST(a.getLeftNode(), min, a.data);

		boolean checkR = checkBST(a.getRightNode(), a.data, max);

		return (check && checkL && checkR);
	}

	//create a minimal BST given a sorted array
	//recursive
	public static Node createBST(int[] array1)
	{
		int len = array1.length;

		int middle = len / 2;

		Node a = new Node(array1[middle]);

		//System.out.printf("Node %d\n", a.data);

		int left_len = len - middle;

		if ((len % 2) > 0)	//for odd numbered lists
		{
			left_len = left_len - 1;
		}
		
		if (left_len == 1)
		{
			a.left_child = new Node(array1[0]);
			//System.out.printf("left child = %d\n", a.left_child.data);
		}
		else
		{
			int[] left_array = new int[left_len];

			for (int x = 0; x < left_len; x++)
			{
				left_array[x] = array1[x];
			}

			//System.out.printf("left recursive call, size %d\n", left_array.length);
			a.left_child = Node.createBST(left_array);
		}

		int right_len = len - middle - 1;

		if (right_len == 0)  //sometimes there is no right child
		{
			//System.out.printf("Right child = null\n");
			return null;
		}
		if (right_len == 1)
		{
			a.right_child = new Node(array1[len-1]);
			//System.out.printf("Right child = %d\n", a.right_child.data);
		}
		else
		{		
			int[] right_array = new int[right_len];

			for (int x = 0; x < right_len; x++)
			{
				right_array[x] = array1[x+middle+1];
			}

			//System.out.printf("right recursive call, size %d\n", right_array.length);
			a.right_child = Node.createBST(right_array);	
		}

		return a;
	}

	public static void main(String[] args)
	{
		int[] test = {1,2,3,4,5,6};

		Node bst = Node.createBST(test);

		System.out.println(Node.checkBST(bst,0,100));

		int[] test2 = {1,2,3,4,5,6,7,8,9};

		bst = Node.createBST(test2);

		System.out.println(Node.checkBST(bst,0,100));

		// create  a tree thats not a bst
		Node a = new Node(1);
		Node b = new Node(2);
		Node c = new Node(3);
		Node d = new Node(4);
		Node e = new Node(5);

		a.setLeftNode(e);
		a.setRightNode(c);
		b.setLeftNode(a);
		d.setRightNode(e);
		b.setRightNode(d);

		System.out.println(Node.checkBST(b,0,100));		
	}
}