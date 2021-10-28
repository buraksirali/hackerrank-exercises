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
     * Complete the 'acmTeam' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts STRING_ARRAY topic as parameter.
     */

    public static List<int> acmTeam(List<string> topic)
    {
        List<int> result = new List<int>();
        
        int max = 0;
        
        int bestTeamCount = 0;
        
        for(int index = 0; index < topic.Count - 1; index++)
        {
            for(int idxSec = index; idxSec < topic.Count; idxSec++)
            {
                int count = 0;
                
                for(int ch = 0; ch < topic[index].Length; ch++)
                {
                    if (topic[index][ch] == '1' || topic[idxSec][ch] == '1')
                    {
                        count++;
                    }
                }
                
                if (count > max)
                {
                    max = count;
                    
                    bestTeamCount = 1;
                }
                else if (count == max)
                {
                    bestTeamCount++;
                }
            }
        }
        
        result.Add(max);
        result.Add(bestTeamCount);
        
        return result;
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

        List<string> topic = new List<string>();

        for (int i = 0; i < n; i++)
        {
            string topicItem = Console.ReadLine();
            topic.Add(topicItem);
        }

        List<int> result = Result.acmTeam(topic);

        textWriter.WriteLine(String.Join("\n", result));

        textWriter.Flush();
        textWriter.Close();
    }
}
