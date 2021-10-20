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
     * Complete the 'designerPdfViewer' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY h
     *  2. STRING word
     */

    public static int designerPdfViewer(List<int> h, string word)
    {
        byte[] wordInBytes = Encoding.ASCII.GetBytes(word);
        int[] wordIndexes = wordInBytes.Select(value => Convert.ToInt32(value) - 97).ToArray();
        
        int minHeight = h[wordIndexes[0]];
        int maxHeight = h[wordIndexes[0]];
        
        for(int index = 1; index < word.Length; index++)
        {
            int height = h[wordIndexes[index]];
            
            if (height < minHeight)
            {
                minHeight = height;
            }
            else if (height > maxHeight)
            {
                maxHeight = height;
            }
        }
        
        return minHeight * maxHeight * word.Length;
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        List<int> h = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(hTemp => Convert.ToInt32(hTemp)).ToList();

        string word = Console.ReadLine();

        int result = Result.designerPdfViewer(h, word);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
