#!/usr/bin/env python3
import inkex

class PathBinder(inkex.Effect):
    def add_arguments(self, pars):
        pars.add_argument("--bridge_width", type=float, default=5.0, help="Bridge width")
        pars.add_argument("--bridge_interval", type=float, default=50.0, help="Bridge interval")

    def effect(self):
        self.msg(f"Bridge width: {self.options.bridge_width}")
        self.msg(f"Bridge interval: {self.options.bridge_interval}")
        # TODO: Add bridge logic here

if __name__ == '__main__':
    PathBinder().run()
