using Xunit;

namespace advent_of_code_tests
{
    public class Day1UnitTests
    {
        [Fact]
        public void IncreasedDepthsSuccess()
        {
            int[] input1 = { 199, 200, 208, 210, 200, 207, 240, 269, 260, 263 };
            int ans1 = advent_of_code.Day1.IncreasedDepths(input1);
            Assert.Equal(7, ans1);

            int[] input2 = { 139, 351, 276, 60, 196, 381, 169, 448, 173, 43, 208, 69, 288, 304, 416, 197, 471, 398, 326, 154 };
            int ans2 = advent_of_code.Day1.IncreasedDepths(input2);
            Assert.Equal(9, ans2);
        }

        [Fact]
        public void IncreasedDepthsFail()
        {
            int[] input = { 139, 351, 276, 60, 196, 381, 169, 448, 173, 43, 208, 69, 288, 304, 416, 197, 471, 398, 326, 154 };
            int ans = advent_of_code.Day1.IncreasedDepths(input);
            Assert.NotEqual(7, ans);
        }
    }
}
     
