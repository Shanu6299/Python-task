from typing import List, Tuple, Optional

def sanitize_query(query: str) -> str:
    """Sanitize the search query for PubMed API.

    Args:
        query (str): The raw search query.

    Returns:
        str: The sanitized query with spaces replaced by plus signs.
    """
    return query.replace(" ", "+")

def extract_non_academic_authors(authors: List[dict]) -> Tuple[List[str], List[str], Optional[str]]:
    """Extract non-academic authors and their company affiliations from the authors list.

    Args:
        authors (List[dict]): List of author dictionaries containing name and affiliation.

    Returns:
        Tuple[List[str], List[str], Optional[str]]: A tuple containing:
            - List of non-academic author names
            - List of company affiliations
            - Corresponding author email (if available)
    """
    non_academic_authors = []
    companies = []
    corresponding_email = None

    academic_keywords = [
        "university", "college", "institute", "school", "academia",
        "hospital", "medical center", "clinic", "laboratory", "research center"
    ]

    company_keywords = [
        "pharma", "biotech", "therapeutics", "pharmaceuticals", "inc",
        "corp", "llc", "ltd", "limited", "biosciences", "medicines"
    ]

    for author in authors:
        name = author.get("name", "")
        affiliation = author.get("affiliation", "").lower()
        email = author.get("email")

        # Check if author is from a company
        is_academic = any(keyword in affiliation for keyword in academic_keywords)
        is_company = any(keyword in affiliation for keyword in company_keywords)

        if is_company and not is_academic:
            non_academic_authors.append(name)
            companies.append(affiliation)

            # Store the first company author's email as corresponding email
            if email and not corresponding_email:
                corresponding_email = email

    return non_academic_authors, companies, corresponding_email

def format_author_name(name: str) -> str:
    """Format author name in a consistent way.

    Args:
        name (str): Author name in any format.

    Returns:
        str: Formatted author name (Last, First MI)
    """
    parts = name.split()
    if len(parts) < 2:
        return name

    last_name = parts[-1]
    first_name = parts[0]
    middle_initial = parts[1][0] + "." if len(parts) > 2 else ""

    return f"{last_name}, {first_name} {middle_initial}".strip()
