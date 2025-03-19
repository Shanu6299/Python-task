from typing import List, Dict, Tuple
from .utils import extract_non_academic_authors, format_author_name


def filter_non_academic_authors(papers: List[Dict]) -> List[Dict]:
    """Filter papers to include only those with at least one non-academic author.

    Args:
        papers (List[Dict]): List of papers with author information.

    Returns:
        List[Dict]: Filtered list of papers with non-academic authors.
    """
    filtered_papers = []

    for paper in papers:
        non_academic_authors, companies, email = extract_non_academic_authors(paper["Authors"])

        if non_academic_authors:
            # Format author names consistently
            formatted_authors = [format_author_name(author) for author in non_academic_authors]
            
            filtered_papers.append({
                "PubmedID": paper["PubmedID"],
                "Title": paper["Title"],
                "Publication Date": paper["Publication Date"],
                "Non-academic Author(s)": ", ".join(formatted_authors),
                "Company Affiliation(s)": ", ".join(companies),
                "Corresponding Author Email": email or "Not available"
            })

    return filtered_papers
