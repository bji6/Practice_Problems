// ben isenberg 9/17/2016
import java.util.*;

//implement animal shelter class
class AnimalShelter
{
	LinkedList<Integer> cats;
	LinkedList<Integer> dogs;

	public AnimalShelter()
	{
		cats = new LinkedList<Integer>();
		dogs = new LinkedList<Integer>();
	}

	void enqueue(String type)
	{
		if (type == "cat")
		{
			cats.add(0);
		}
		if (type == "dog")
		{
			dogs.add(0);
		}

		incrementDay();
	}

	String dequeueAny()
	{
		int oldest = 0;
		int oldestIndex = 0;
		String type = "";

		for (int x = 0; x < cats.size(); x++)
		{
			if (cats.get(x) > oldest)
			{
				oldest = cats.get(x);
				oldestIndex = x;
				type = "cat";
			}
		}
		for (int x = 0; x < dogs.size(); x++)
		{
			if (dogs.get(x) > oldest)
			{
				oldest = dogs.get(x);
				oldestIndex = x;
				type = "dog";
			}
		}

		if (type == "dog")
		{
			dogs.remove(oldestIndex);
		}
		else
		{
			cats.remove(oldestIndex);	
		}

		System.out.printf("You get a %s that is %d old\n", type, oldest);

		return type;
	}

	String dequeueCat()
	{
		int oldest = 0;
		int oldestIndex = 0;
		String type = "cat";

		for (int x = 0; x < cats.size(); x++)
		{
			if (cats.get(x) > oldest)
			{
				oldest = cats.get(x);
				oldestIndex = x;
				type = "cat";
			}
		}
		
		cats.remove(oldestIndex);

		System.out.printf("You get a %s that is %d old\n", type, oldest);

		return type;
	}

	String dequeueDog()
	{
		int oldest = 0;
		int oldestIndex = 0;
		String type = "dog";

		for (int x = 0; x < dogs.size(); x++)
		{
			if (dogs.get(x) > oldest)
			{
				oldest = dogs.get(x);
				oldestIndex = x;
				type = "dog";
			}
		}
		
		dogs.remove(oldestIndex);

		System.out.printf("You get a %s that is %d old\n", type, oldest);

		return type;
	}	

	void incrementDay()
	{
		int len = cats.size();

		for (int x = 0; x < len; x++)
		{
			cats.set(x, cats.get(x) + 1);
		}
		len = dogs.size();
		for (int x = 0; x < len; x++)
		{
			dogs.set(x, dogs.get(x) + 1);
		}
	}

	void print()
	{
		System.out.println(cats);
		System.out.println(dogs);
	}

	public static void main(String[] args)
	{
		AnimalShelter test = new AnimalShelter();
		test.enqueue("cat");
		test.enqueue("dog");
		test.enqueue("cat");
		test.enqueue("cat");
		test.enqueue("dog");
		test.dequeueAny();
		test.enqueue("cat");
		test.enqueue("cat");
		test.enqueue("dog");
		test.dequeueDog();
		test.dequeueAny();
		test.dequeueCat();
		test.dequeueDog();

		test.print();
	}
}