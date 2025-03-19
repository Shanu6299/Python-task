# PubMed Paper Analyzer

## Overview
PubMed Paper Analyzer is a specialized tool designed to identify research papers that bridge academia and industry. It searches PubMed for scientific publications and identifies papers where at least one author is affiliated with a pharmaceutical or biotech company.

## Key Features
- Efficient PubMed database searching using official NCBI E-utilities
- Smart detection of industry-affiliated authors
- Comprehensive author affiliation analysis
- Flexible output options (CSV export or console display)
- Debug mode for troubleshooting

## Requirements
- Python 3.10 or higher
- Poetry for dependency management
- PubMed API key (get it from NCBI)

## Setup
1. Clone this repository:
```bash
git clone <repository-url>
cd pubmed-paper-analyzer
```

2. Set up your environment:
- Install Poetry if you haven't already
- Set your PubMed API key:
  ```bash
  export PUBMED_API_KEY="your-api-key-here"
  ```

3. Install dependencies:
```bash
poetry install
```

## Usage
Basic command structure:
```bash
poetry run get-papers-list "your search query" [options]
```

Options:
- `-f, --file`: Save results to a CSV file
- `-d, --debug`: Enable debug mode for detailed output
- `-h, --help`: Display help information

Example:
```bash
poetry run get-papers-list "CRISPR cancer therapy" -f results.csv
```

## Output Format
The tool generates a CSV file with the following columns:
- PubMed ID
- Paper Title
- Publication Date
- Non-academic Author(s)
- Company Affiliation(s)
- Corresponding Author Email

## Rate Limiting
The tool respects PubMed's API rate limits by default:
- Maximum 3 requests per second
- Batch processing of paper IDs

## Error Handling
- Graceful handling of API errors
- Clear error messages for troubleshooting
- Debug mode for detailed logging

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is available under the MIT License.
