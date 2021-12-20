using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace advent_of_code
{
    public class Day05
    {
        public static void Start()
        {
            string[] inputLines = File.ReadAllLines("Day05RealInput.txt");

            var lines = inputLines.Select(line => line.Split(" -> ")
                                                      .Select(coord => coord.Split(",").Select(int.Parse))
                                                      .Select(coord => (coord.First(), coord.Last())))
                                  .Select(coord => (coord.First(), coord.Last()));

            var allCoords = lines.Select(line => getPointsOnLine(line)).SelectMany(x => x);

            var groupedCoords = allCoords.GroupBy(x => x).Where(group => group.Count() > 1).Count();

            Console.WriteLine($"Part 1 Answer: {groupedCoords}");
        }

        public static IEnumerable<(int, int)> getPointsOnLine(((int x, int y) start, (int x, int y) end) line)
        {
            var xRange = Enumerable.Range(line.start.x < line.end.x ? line.start.x : line.end.x, Math.Abs(line.start.x - line.end.x) + 1);
            var yRange = Enumerable.Range(line.start.y < line.end.y ? line.start.y : line.end.y, Math.Abs(line.start.y - line.end.y) + 1);

            xRange = line.start.x < line.end.x ? xRange : xRange.Reverse();
            yRange = line.start.y < line.end.y ? yRange : yRange.Reverse();

            if (line.start.x == line.end.x || line.start.y == line.end.y)
            {
                return xRange.SelectMany(x => yRange.Select(y => (x, y)));
            } else
            {
                return xRange.Zip(yRange, (x, y) => (x, y));
            }
        }
    }
}
