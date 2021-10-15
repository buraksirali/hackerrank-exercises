using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Result
{

    /*
     * Complete the 'getTotalX' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY a
     *  2. INTEGER_ARRAY b
     */

    public static int getTotalX(List<int> array, List<int> targets)
    {
        int firstFactor = array.ElementAt(0);

        for (int index = 1; index < array.Count(); index++)
        {
            firstFactor = lcm(firstFactor, array.ElementAt(index));
        }

        int result = 0;
        int min = targets.Min();
        
        List<int> factors = GetNums(firstFactor, min);
        
        foreach (int num in factors)
        {
            int count = 0;
            
            foreach(int target in targets) {
                count += target % num;
            }
            
            if (count == 0)
            {
                result++;
            }
        }
        
        return result;
    }
    
    private static List<int> GetNums(int firstFactor, int maxNum)
    {
        List<int> factors = new List<int>();
        
        for(int index = 1; index <= maxNum; index++)
        {
            int value = firstFactor * index;
            
            if (value > maxNum)
            {
                break;
            }
            else
            {
                factors.Add(value);
            }
        }
        
        return factors;
    }
    
    static int gcf(int a, int b)
    {
        while (b != 0)
        {
            int temp = b;
            b = a % b;
            a = temp;
        }
        
        return a;
    }

    static int lcm(int a, int b)
    {
        return (a / gcf(a, b)) * b;
    }
    
}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string[] firstMultipleInput = Console.ReadLine().TrimEnd().Split(' ');

        int n = Convert.ToInt32(firstMultipleInput[0]);

        int m = Convert.ToInt32(firstMultipleInput[1]);

        List<int> arr = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(arrTemp => Convert.ToInt32(arrTemp)).ToList();

        List<int> brr = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(brrTemp => Convert.ToInt32(brrTemp)).ToList();

        int total = Result.getTotalX(arr, brr);

        textWriter.WriteLine(total);

        textWriter.Flush();
        textWriter.Close();
    }
}