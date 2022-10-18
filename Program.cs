using System.Diagnostics;

long CPUHeavy(long number)
{
    long count = 0;
	for (long i = 0; i <= number; i++)
	{
		count += i;
	}
	return count;
}

void ParallelAggregation(long[] numbers)
{
	var result = numbers.AsParallel().Select(x => CPUHeavy(x)).Sum();
	Console.WriteLine(result);
}

void BrewCoffee()
{
    Thread.Sleep(4000);
}

void MakeToast()
{
	Thread.Sleep(2000);
}

void FryEggs()
{
    Thread.Sleep(3000);
}

void ParallelBreakfast()
{    
    Parallel.Invoke(BrewCoffee, MakeToast, FryEggs);
}

void PrintTime(Action ac)
{
    var sw = Stopwatch.StartNew();
	ac();
	sw.Stop();
	var time = sw.ElapsedMilliseconds;
    Console.WriteLine($"{Math.Round(time / 1000.0, 3)} secs");
}


/*long[] numbers = new long[20_000_000];
for (int i = 0; i < numbers.Length; i++)
{
	numbers[i] = 10;
}
PrintTime(()=> ParallelAggregation(numbers));*/
PrintTime(ParallelBreakfast);