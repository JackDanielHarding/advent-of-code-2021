using System;
using System.Diagnostics;
using System.IO;
using System.Linq;

namespace advent_of_code
{
    public class Day02
    {
        public static void Start()
        {
            // Part 1

            string[] commands = File.ReadAllLines("Day02RealInput.txt");

            SubmarinePositionBasic subPosBasic = new();

            moveSubmarine(commands, subPosBasic);

            Console.WriteLine($"Part 1 Answer: {subPosBasic.HorizontalPosition * subPosBasic.Depth}");

            // Part 2

            SubmarinePositionAdvanced subPosAdvanced = new();

            moveSubmarine(commands, subPosAdvanced);

            Console.WriteLine($"Part 2 Answer: {subPosAdvanced.HorizontalPosition * subPosAdvanced.Depth}");

        }

        static void moveSubmarine(String[] commands, SubmarinePosition subPos)
        {
            var splitCommands = commands.Select(x => x.Split(" "));

            foreach (String[] command in splitCommands)
            {

                int magnitude = Int32.Parse(command[1]);

                switch (command[0])
                {
                    case "forward":
                        subPos.forward(magnitude);
                        break;
                    case "down":
                        subPos.down(magnitude);
                        break;
                    case "up":
                        subPos.up(magnitude);
                        break;
                    default:
                        Trace.TraceError("invalid command in input");
                        break;
                }
            }
        }
    }

    interface SubmarinePosition
    {
        public void forward(int magnitude);
        public void down(int magnitude);
        public void up(int magnitude);
    }

    class SubmarinePositionBasic : SubmarinePosition 
    {
        public int HorizontalPosition { get; private set; } = 0;
        public int Depth { get; private set; } = 0;

        public void forward(int magnitude)
        {
            HorizontalPosition += magnitude;
        }

        public void down(int magnitude)
        {
            Depth += magnitude;
        }

        public void up(int magnitude)
        {
            Depth -= magnitude;
        }
    }

    class SubmarinePositionAdvanced : SubmarinePosition
    {
        public int HorizontalPosition { get; private set; } = 0;
        public int Depth { get; private set; } = 0;
        public int Aim { get; private set; } = 0;

        public void forward(int magnitude)
        {
            HorizontalPosition += magnitude;
            Depth += Aim * magnitude;
        }

        public void down(int magnitude)
        {
            Aim += magnitude;
        }

        public void up(int magnitude)
        {
            Aim -= magnitude;
        }
    }
}
