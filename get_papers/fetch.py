import requests
import time
import os
from typing import List, Dict


def fetch_papers(query: str, debug: bool = False) -> List[Dict]:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 100,
        "api_key": os.getenv("PUBMED_API_KEY")  # Get API key from environment variable
    }

    try:
        response = requests.get(base_url, params=params)

        if debug:
            print(f"API Request URL: {response.url}")
            print(f"Response Status Code: {response.status_code}")

        response.raise_for_status()
        data = response.json()

        if "error" in data:
            raise Exception(f"PubMed API error: {data['error']}")

        paper_ids = data.get("esearchresult", {}).get("idlist", [])

        if not paper_ids and debug:
            print("No papers found for the given query")

        return fetch_paper_details(paper_ids, debug)

    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching data from PubMed API: {str(e)}")
    except ValueError as e:
        raise Exception(f"Error parsing PubMed API response: {str(e)}")


def fetch_paper_details(paper_ids: List[str], debug: bool) -> List[Dict]:
    if not paper_ids:
        return []

    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    papers = []

    # Process papers in batches to avoid API limits
    batch_size = 50
    for i in range(0, len(paper_ids), batch_size):
        batch = paper_ids[i:i + batch_size]
        params = {
            "db": "pubmed",
            "id": ",".join(batch),
            "retmode": "json",
            "api_key": os.getenv("PUBMED_API_KEY")  # Get API key from environment variable
        }

        try:
            response = requests.get(base_url, params=params)
            if debug:
                print(f"Fetching details for papers {i+1}-{i+len(batch)}")
                print(f"API Request URL: {response.url}")

            response.raise_for_status()
            data = response.json()

            if "error" in data:
                raise Exception(f"PubMed API error: {data['error']}")

            results = data.get("result", {})
            for paper_id in batch:
                if paper_id in results:
                    paper_data = results[paper_id]
                    papers.append({
                        "PubmedID": paper_id,
                        "Title": paper_data.get("title", ""),
                        "Publication Date": paper_data.get("pubdate", ""),
                        "Authors": [{
                            "name": author.get("name", ""),
                            "affiliation": author.get("affil", ""),
                            "email": author.get("email", "")
                        } for author in paper_data.get("authors", [])]
                    })

            # Respect API rate limits
            time.sleep(0.34)  # ~3 requests per second

        except requests.exceptions.RequestException as e:
            if debug:
                print(f"Error fetching details for batch {i+1}-{i+len(batch)}: {str(e)}")
            continue
        except ValueError as e:
            if debug:
                print(f"Error parsing response for batch {i+1}-{i+len(batch)}: {str(e)}")
            continue

    return papers
