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
     * Complete the 'pickingNumbers' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY a as parameter.
     */

    public static int pickingNumbers(List<int> a)
    {
        Dictionary<int, int> numCounts = new Dictionary<int, int>(); 
        
        foreach(int num in a)
        {
            if (numCounts.Keys.Contains(num))
            {
                numCounts[num]++;
            }
            else
            {
                numCounts[num] = 1;
            }
        }
        
        int max = 0;
        
        List<int> keys = numCounts.Keys.ToList();
        keys.Sort();
        
        foreach(int key in keys)
        {
            int val = 0;
            
            if (keys.Contains(key + 1))
            {
                val = numCounts[key] + numCounts[key + 1];
            }
            else
            {
                val = numCounts[key];
            }
            
            if (val > max)
            {
                max = val;
            }
        }
        
        return max;
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine().Trim());

        List<int> a = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(aTemp => Convert.ToInt32(aTemp)).ToList();

        int result = Result.pickingNumbers(a);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
