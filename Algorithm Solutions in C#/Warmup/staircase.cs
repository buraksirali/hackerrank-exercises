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
     * Complete the 'staircase' function below.
     *
     * The function accepts INTEGER n as parameter.
     */

    public static void staircase(int n)
    {
        string result = "";
        
        for (int index_row = 1; index_row <= n; index_row++) {
            for (int index = 0; index < n - index_row; index++) {
                result += " ";
            }
            
            for (int index = 0; index < index_row; index++) {
                result += "#";
            }
            
            if (index_row != n) {
                result += "\n";
            }
        }
        
        Console.WriteLine(result);
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        int n = Convert.ToInt32(Console.ReadLine().Trim());

        Result.staircase(n);
    }
}
