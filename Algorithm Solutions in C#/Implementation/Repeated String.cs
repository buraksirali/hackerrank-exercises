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
     * Complete the 'repeatedString' function below.
     *
     * The function is expected to return a LONG_INTEGER.
     * The function accepts following parameters:
     *  1. STRING s
     *  2. LONG_INTEGER n
     */

    public static long repeatedString(string s, long n)
    {
        List<long> aByIndex = new List<long>();
        
        long count = 0;
        foreach(char c in s.ToCharArray())
        {
            if (c == 'a')
            {
                count++;
            }
            
            aByIndex.Add(count);
        }
        
        long repetition = n / Convert.ToInt64(s.Length);
        
        long aCount =  repetition * aByIndex[s.Length - 1];
        
        if (n % s.Length > 0)
        {
            int len = (int)(n % s.Length);
            
            aCount += aByIndex[len - 1];
        }
        
        return aCount;
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string s = Console.ReadLine();

        long n = Convert.ToInt64(Console.ReadLine().Trim());

        long result = Result.repeatedString(s, n);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
