using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace advent_of_code
{
    public class Day06
    {
        public static void Start()
        {
            string[] inputLines = File.ReadAllLines("Day06RealInput.txt");
            string input = inputLines.First();
            CalculateSpawn(input, 256);
        }

        public static void CalculateSpawn(string input, int days)
        {
            List<int> starterFish = new(input.Split(",").Select(int.Parse));

            var fish = new Dictionary<int, double>()
            {
                 {0, 0},
                 {1, 0},
                 {2, 0},
                 {3, 0},
                 {4, 0},
                 {5, 0},
                 {6, 0},
                 {7, 0},
                 {8, 0}
            };

            foreach(int starter in starterFish)
            {
                fish[starter]++;
            }

            foreach (int day in Enumerable.Range(1, days))
            {
                double newFish = 0;

                foreach (int key in fish.Keys)
                {
                    if(key == 0)
                    {
                        newFish = fish[key];
                    } else
                    {
                        fish[key - 1] = fish[key];
                        fish[key] = 0;
                    }
                }
                fish[8] += newFish;
                fish[6] += newFish;
            }

            Console.WriteLine($"{fish.Values.Sum()} fish in {days} days");
        }
    }
}
