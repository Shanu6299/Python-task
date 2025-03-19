#!/usr/bin/env python
import argparse
import csv
from get_papers.fetch import fetch_papers
from get_papers.filter import filter_non_academic_authors


def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename", default=None)
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    
    args = parser.parse_args()

    # Fetch papers using PubMed API
    papers = fetch_papers(args.query, args.debug)

    # Filter non-academic authors
    filtered_papers = filter_non_academic_authors(papers)

    # Output results to file or console
    if args.file:
        with open(args.file, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=filtered_papers[0].keys())
            writer.writeheader()
            writer.writerows(filtered_papers)
        print(f"Results saved to {args.file}")
    else:
        for paper in filtered_papers:
            print(paper)


if __name__ == "__main__":
    main()
