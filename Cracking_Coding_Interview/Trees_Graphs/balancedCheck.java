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

	public static boolean checkBalanced(Node head)
	{
		int[] results = checkBalancedRecursive(head);

		if (results[0] == 1)
		{
			return true;
		}

		return false;
	}

	//recursive function to check if a binary tree is balanced
	// this means that every node's subtrees are balanced, dont differ in height by more than 1
	public static int[] checkBalancedRecursive(Node a)
	{
		int[] results = new int[2];

		//base case
		if (a == null)
		{
			results[0] = 1;  //subtree is balanced, no nodes
			results[1] = 0;  //subtree height is 0, no nodes
			return results;
		}

		int[] results_left = checkBalancedRecursive(a.getLeftNode());

		int[] results_right = checkBalancedRecursive(a.getRightNode());

		if (Math.abs(results_left[1]-results_right[1]) <= 1) //check if subtrees are balanced
		{
			results[0] = 1;  //this node's subtrees are balanced
		}
		else
		{
			results[0] = 0;  //this node's subtrees are NOT balanced
		}

		results[1] = Math.max(results_left[1],results_right[1]) + 1;

		return results;
	}
	
	public static void main(String[] args)
	{
		Node a = new Node(1);
		Node b = new Node(2);
		Node c = new Node(3);
		Node d = new Node(4);
		Node e = new Node(5);
		Node f = new Node(6);
		Node g = new Node(7);
		Node h = new Node(8);

		//build my binary tree
		f.setLeftNode(g);
		d.setLeftNode(f);
		b.setLeftNode(d);
		b.setRightNode(e);
		a.setLeftNode(b);
		a.setRightNode(c);
		
		//d.setLeftNode(h);
		//b.setLeftNode(d);
		//b.setRightNode(e);
		//c.setLeftNode(f);
		//c.setRightNode(g);
		//a.setLeftNode(b);
		//a.setRightNode(c);

		boolean checkIfBalanced = checkBalanced(a);

		System.out.println("Is tree balanced ?  " + checkIfBalanced);
	}
}