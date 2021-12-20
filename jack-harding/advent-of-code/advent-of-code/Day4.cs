using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;

namespace advent_of_code
{
    public class Day4
    {
        public static void Start()
        {
            Trace.Listeners.Add(new TextWriterTraceListener(Console.Out));
            Trace.AutoFlush = true;

            string[] inputLines = File.ReadAllLines("Day4RealInput.txt");

            IEnumerable<string> draws = inputLines[0].Split(",");

            var boards = inputLines.Skip(1)
                                .Where(line => !string.IsNullOrWhiteSpace(line))
                                .Select((row, index) => new { row, index })
                                .GroupBy(g => g.index / 5, i => i.row)
                                .Select(board => (board, false, 0));

            int firstScore = 0;
            int lastScore = 0;
            string latestDraw = "0";
            var boardsToRemove = new List<IEnumerable<string>>();

            for (int i = 1; i <= draws.Count(); i++)
            {
                var drawsSoFar = draws.Take(i);
                latestDraw = drawsSoFar.Last();

                boards = boards.Where(board => !board.Item2)
                      .Select(board => (board.board, checkForWin(board.board, drawsSoFar), getBingoScore(board.board, drawsSoFar)));

                if(boards.Where(board => board.Item2).Any())
                {
                    lastScore = boards.Where(board => board.Item2).First().Item3 * int.Parse(latestDraw);

                    if (firstScore == 0)
                    {
                        firstScore = lastScore;
                    }
                }
            }

            var latestDrawInt = int.Parse(latestDraw);

            Console.WriteLine($"Part 1 Answer: {firstScore}");
            Console.WriteLine($"Part 2 Answer: {lastScore}");

        }

        private static int getBingoScore(IEnumerable<string> board, IEnumerable<string> draws)
        {
            return board.Select(row => new List<string>(row.Split(" ").Where(element => !string.IsNullOrWhiteSpace(element))))
                                         .SelectMany(x => x)
                                         .Except(draws)
                                         .Select(int.Parse)
                                         .Sum();
        }

        private static bool checkForWin(IEnumerable<string> board, IEnumerable<string> draws)
        {
            
            var rowsandcolumns = board.Select(row => new List<string>(row.Split(" ").Where(element => !string.IsNullOrWhiteSpace(element))));

            bool rowWin = rowsandcolumns.Any(row => row.Intersect(draws).Count() == row.Count());
            bool columnWin = false;

            for (int i = 0; i < rowsandcolumns.Count(); i++)
            {
                if (rowsandcolumns.Select(row => row[i]).Intersect(draws).Count() == rowsandcolumns.Count())
                {
                    columnWin = true;
                    break;
                }
            }

            return rowWin || columnWin;
        }
    }
}
