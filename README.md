# PathBinder - Bridged Stencil Generator

PathBinder is an Inkscape extension that automatically generates bridges in stencil designs to ensure they remain structurally intact when cut or printed. This tool is essential for creating professional stencils that won't fall apart during use.

## What It Does

PathBinder solves the common problem in stencil design where interior parts of letters or shapes become disconnected "islands" that fall out when the stencil is cut. The extension automatically analyzes your paths and strategically places narrow bridges to connect all parts while maintaining the visual integrity of your design.

### Key Features

- **Automatic Bridge Generation**: Intelligently places bridges to connect disconnected path segments
- **Configurable Bridge Width**: Adjust bridge thickness (default: 5px) to match your cutting method
- **Customizable Bridge Spacing**: Control bridge placement interval (default: 50px) for optimal structural support
- **Preserves Design Integrity**: Maintains the visual appearance while ensuring structural stability
- **Professional Results**: Creates production-ready stencils suitable for laser cutting, vinyl cutting, or hand cutting

### Perfect For

- **Sign makers** creating letter stencils with enclosed shapes (A, B, D, O, P, Q, R, etc.)
- **Artists** designing decorative stencils with complex interior details
- **Crafters** making reusable templates for painting or etching
- **Manufacturers** producing industrial marking stencils
- **Educators** creating teaching aids and templates

## How It Works

1. Select the path(s) you want to convert into a bridged stencil
2. Go to **Extensions > Render & Stencil > PathBinder - Bridged Stencil Generator**
3. Configure your bridge settings:
   - **Bridge Width**: How thick the connecting bridges should be
   - **Bridge Interval**: Distance between bridge placements
4. Click Apply to generate your bridged stencil

The extension analyzes your selected paths and automatically determines where bridges are needed to prevent any parts from becoming disconnected.

## Installation

### Prerequisites
- Inkscape (version 1.0 or later)
- Python 3.6+ (usually included with Inkscape)

### Install the Extension

1. **Download** the extension files from this repository
2. **Locate** your Inkscape extensions directory:
   - **Windows**: `%APPDATA%\inkscape\extensions\`
   - **macOS**: `~/.config/inkscape/extensions/`
   - **Linux**: `~/.config/inkscape/extensions/`
3. **Copy** both `pathbinder.inx` and `pathbinder.py` to the extensions directory
4. **Restart** Inkscape
5. **Find** the extension under **Extensions > Render & Stencil > PathBinder**

## Development

This project is currently in active development. The core bridge generation algorithm is being implemented.

### Development Environment Setup

1. **Clone** this repository:
   ```bash
   git clone https://github.com/johnsirmon/inkscape-pathbinder.git
   cd inkscape-pathbinder
   ```

2. **Create** the conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate pathbinder
   ```

3. **Open** in VS Code with the included workspace settings for optimal development experience

### Project Structure

```
inkscape-pathbinder/
├── extensions/
│   ├── pathbinder.inx    # Inkscape extension definition
│   └── pathbinder.py     # Main extension logic
├── tests/                # Unit tests (planned)
├── docs/                 # Documentation (planned)
├── environment.yml       # Conda environment specification
└── .vscode/settings.json # VS Code workspace settings
```

## Roadmap

- [ ] Core bridge generation algorithm
- [ ] Multi-layer stencil support
- [ ] Complexity analysis and optimization
- [ ] Print layout and nesting features
- [ ] Advanced bridge placement strategies
- [ ] GUI improvements and preview functionality

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## License

This project is licensed under the terms specified in the LICENSE file.

## Support

If you find this extension useful, please consider starring the repository and sharing it with others in the maker community!
