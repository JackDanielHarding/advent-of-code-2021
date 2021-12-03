using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;

namespace advent_of_code
{
    public class Day3
    {
        public static void Start()
        {
            Trace.Listeners.Add(new TextWriterTraceListener(Console.Out));
            Trace.AutoFlush = true;

            string[] inputs = File.ReadAllLines("Day3RealInput.txt");

            //Part1(inputs);

            var oxygenGenRating = GetStuff(inputs).First();
            Trace.TraceInformation($"Oxygen Generation Rating: {oxygenGenRating}");

            int oxygenGenRatingInt = Convert.ToInt32(oxygenGenRating, 2);

            var co2ScrubRating = GetStuff(inputs, flip: true).First();
            Trace.TraceInformation($"CO2 Scrubber Rating: {co2ScrubRating}");

            int co2ScrubRatingInt = Convert.ToInt32(co2ScrubRating, 2);

            Console.WriteLine($"Part 2 Answer: {oxygenGenRatingInt * co2ScrubRatingInt}");
        }

        public static IEnumerable<bool> BoolEnumerableFromCharEnumerable(IEnumerable<char> chars)
        {
            List<bool> bools = new();

            foreach(char character in chars)
            {
                if (character == '0')
                {
                    bools.Add(false);
                } else
                {
                    bools.Add(true);
                }
            }

            return bools;
        }

        public static void Part1(IEnumerable<string> inputs)
        {
            List<bool> gammaRateBinary = new();

            for (int i = inputs.First().Length - 1; i >= 0; i--)
            {
                char mostCommonChar = getMostCommonChar(inputs, i);
                gammaRateBinary.Add(mostCommonChar == '1' ? true : false);
            }

            BitArray gammaRateBitArray = new BitArray(gammaRateBinary.ToArray());
            int[] array = new int[1];
            gammaRateBitArray.CopyTo(array, 0);
            int gammaRateInt = array[0];

            Trace.TraceInformation($"{gammaRateInt}");

            BitArray epsilonBitArray = gammaRateBitArray.Not();
            epsilonBitArray.CopyTo(array, 0);
            int epsilonRateInt = array[0];

            Trace.TraceInformation($"{epsilonRateInt}");

            Console.WriteLine($"Part 1 Answer: {gammaRateInt * epsilonRateInt}");
        }

        public static IEnumerable<string> GetStuff(IEnumerable<string> inputs, int index = 0, bool flip = false)
        {
            char mostCommon = getMostCommonChar(inputs, index, flip);
            var filteredInputs = inputs.Where(input => input[index] == mostCommon);

            if(filteredInputs.Count() == 1)
            {
                return filteredInputs;
            } else
            {
                return GetStuff(filteredInputs, index + 1, flip);
            }
        }

        public static char getMostCommonChar(IEnumerable<string> inputs, int index, bool flip = false)
        {
            int zeros = 0;
            int ones = 0;

            foreach (string input in inputs)
            {
                if (input[index] == '0')
                {
                    zeros++;
                }
                else if (input[index] == '1')
                {
                    ones++;
                }
            }

            if (flip)
            { 
                return zeros <= ones ? '0' : '1';
            } else
            {
                return ones >= zeros ? '1' : '0';
            }
        }
    }
}
