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
     * Complete the 'encryption' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    public static string encryption(string s)
    {
        int column = (int)Math.Ceiling(Math.Sqrt(s.Length));
        
        List<string> parts = new List<string>();
        
        int pos = 0;
        
        while (pos < s.Length)
        {
            if (s.Length - pos < column)
            {
                parts.Add(s.Substring(pos, s.Length - pos));
            }
            else
            {
                parts.Add(s.Substring(pos, column));
            }
            
            pos += column;
        }
        
        string result = "";
        
        for(int colIndex = 0; colIndex < column; colIndex++)
        {
            foreach(string word in parts)
            {
                if (word.Length > colIndex)
                {
                    result += word[colIndex];
                }
            }
            result += " ";
        }
        
        return result;
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string s = Console.ReadLine();

        string result = Result.encryption(s);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
