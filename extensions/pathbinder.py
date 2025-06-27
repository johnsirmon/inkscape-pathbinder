#!/usr/bin/env python3
"""
PathBinder - Inkscape Extension for Bridged Stencil Generation

This extension automatically generates bridges between selected paths to create
structurally sound stencils that won't fall apart when cut.
"""
import inkex
from inkex import PathElement, Path, Transform
from lxml import etree
import math


class PathBinder(inkex.Effect):
    """Main extension class for generating bridges between paths"""
    
    def add_arguments(self, pars):
        """Add command line arguments for bridge configuration"""
        pars.add_argument("--bridge_width", type=float, default=5.0, help="Bridge width in pixels")
        pars.add_argument("--bridge_interval", type=float, default=50.0, help="Bridge length in pixels")

    def effect(self):
        """Main effect method - generates bridges between selected paths"""
        # Filter selection to only include path elements
        paths = [el for el in self.svg.selection if isinstance(el, PathElement)]

        # Validate that we have at least two paths to bridge
        if len(paths) < 2:
            self.msg("Select at least two paths to bridge between.")
            return

        # Calculate the center point of each selected path's bounding box
        centers = []
        for el in paths:
            bbox = el.bounding_box()
            cx = bbox.left + bbox.width / 2  # Center X coordinate
            cy = bbox.top + bbox.height / 2   # Center Y coordinate
            centers.append((cx, cy))

        # Find the closest pair of paths to bridge between
        min_dist = float("inf")
        pair = (None, None)
        for i in range(len(centers)):
            for j in range(i + 1, len(centers)):
                # Calculate Euclidean distance between centers
                dist = math.hypot(centers[i][0] - centers[j][0], centers[i][1] - centers[j][1])
                if dist < min_dist:
                    min_dist = dist
                    pair = (centers[i], centers[j])

        # Calculate bridge position and orientation
        (x1, y1), (x2, y2) = pair
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2  # Midpoint between the two centers
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))  # Angle to align bridge

        # Create the bridge as a rectangular path element
        bw = self.options.bridge_width    # Bridge width (thickness)
        bl = self.options.bridge_interval # Bridge length
        bridge = etree.Element(inkex.addNS("path", "svg"))
        
        # Generate rectangle path centered at midpoint
        bridge_path = Path.rect(mx - bl / 2, my - bw / 2, bl, bw)
        bridge.set("d", str(bridge_path))
        bridge.set("style", "fill:#000000;stroke:none")  # Black fill, no stroke
        bridge.set("transform", f"rotate({angle},{mx},{my})")  # Rotate to align with path centers

        # Add the bridge to the current layer
        self.svg.get_current_layer().append(bridge)
        self.msg("Bridge inserted between closest paths.")

if __name__ == '__main__':
    PathBinder().run()
