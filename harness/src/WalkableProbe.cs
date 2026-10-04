using System;
using System.Collections.Generic;
using System.Linq;

namespace RRT.TestHarness
{
    public sealed class WalkablePoint
    {
        public float[] Position = Array.Empty<float>();
        public double Distance;
    }

    // Keep the twenty nearest distinct points in a bounded list, regardless of graph size or enumeration order.
    public sealed class WalkableProbe
    {
        public float[] Position = Array.Empty<float>();
        public float Radius;
        public List<WalkablePoint> Points = new List<WalkablePoint>();
        public string? Error;

        public void Consider(float x, float y, float z)
        {
            if (float.IsNaN(x) || float.IsInfinity(x) || float.IsNaN(y) || float.IsInfinity(y) || float.IsNaN(z) || float.IsInfinity(z)) return;
            double dx = (double)x - Position[0], dy = (double)y - Position[1], dz = (double)z - Position[2];
            double distance = Math.Sqrt(dx * dx + dy * dy + dz * dz);
            if (distance > Radius || Points.Count == 20 && distance > Points[19].Distance) return;
            var position = new[] { x, y, z };
            if (Points.Any(p => p.Position.SequenceEqual(position))) return;
            Points.Add(new WalkablePoint { Position = position, Distance = distance });
            Points = Points.OrderBy(p => p.Distance).ThenBy(p => p.Position[0]).ThenBy(p => p.Position[1]).ThenBy(p => p.Position[2]).Take(20).ToList();
        }
    }
}
