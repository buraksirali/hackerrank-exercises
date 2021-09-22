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
     * Complete the 'timeConversion' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    public static string timeConversion(string s)
    {
        string time_stamp = "" + s[s.Length - 2] + s[s.Length - 1];
        string hour = "" + s[0] + s[1];
        
        if (time_stamp == "PM")
        {
            if (hour != "12")
            {
                return $"{int.Parse(hour) + 12}{s.Substring(2, s.Length - 4)}";
            }
        }
        else if (hour == "12")
        {
            return $"00{s.Substring(2, s.Length - 4)}";
        }
        
        return $"{s.Substring(0, s.Length - 2)}";
    }
}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string s = Console.ReadLine();

        string result = Result.timeConversion(s);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
