import bibtexparser
import ads
import time
from tqdm import tqdm
import os

# --- Configuration ---
# The script will look for a file named 'SECRET_BIBTEX' in the same directory.
# This file should contain only your ADS API token.
ADS_TOKEN_FILE = 'SECRET_BIBTEX'
INPUT_BIB_FILE = 'publications_scholar.bib'
OUTPUT_BIB_FILE = 'publications_ads.bib'


def get_ads_token(filename):
    """Reads the ADS API token from a file."""
    if not os.path.exists(filename):
        print(f"Error: API token file '{filename}' not found.")
        print("Please create this file and paste your ADS API token into it.")
        return None
    with open(filename, 'r') as file:
        return file.read().strip()


def fetch_ads_data(entry):
    """
    Fetch the BibTeX and abstract from ADS using DOI or title.
    This function uses the recommended two-step process to avoid API warnings:
    1. SearchQuery to find the paper's bibcode and abstract.
    2. ExportQuery to efficiently retrieve the BibTeX.

    Args:
        entry (dict): A bibtexparser entry dictionary.

    Returns:
        tuple: A tuple containing the bibtex string and the abstract string, or None if not found.
    """
    # Step 1: Find the paper's bibcode and abstract using SearchQuery.
    search_fields = ["bibcode", "abstract"]

    doi = entry.get("doi", "").strip()
    title = entry.get("title", "").strip("{}")

    search_query = None
    if doi:
        search_query = ads.SearchQuery(doi=doi, fl=search_fields)
    elif title:
        search_query = ads.SearchQuery(title=title, fl=search_fields)
    else:
        print(f"Skipping entry '{entry['ID']}' (no DOI or title available).")
        return None

    try:
        # Execute the search and get the first result
        paper = next(search_query)
        bibcode = paper.bibcode
        abstract = paper.abstract

        # Step 2: Use the bibcode to fetch the BibTeX using ExportQuery.
        # This is the recommended method for exporting data and avoids rate limit warnings.
        export_query = ads.ExportQuery(bibcodes=bibcode, format="bibtex")
        bibtex_string = export_query.execute()

        return bibtex_string, abstract

    except StopIteration:
        print(f"No results found on ADS for entry '{entry['ID']}'.")
        return None
    except Exception as e:
        print(
            f"An error occurred while fetching data for '{entry['ID']}': {e}")
        return None


def update_bibtex_file(input_file, output_file):
    """
    Reads a BibTeX file, updates each entry with data from ADS, and saves the result.

    Args:
        input_file (str): Path to the source .bib file.
        output_file (str): Path to save the updated .bib file.
    """
    # Load the original BibTeX file
    try:
        with open(input_file, "r", encoding='utf-8') as f:
            bib_database = bibtexparser.load(f)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return

    updated_entries = []

    print(
        f"Processing {len(bib_database.entries)} entries from '{input_file}'...")
    for entry in tqdm(bib_database.entries, desc="Updating entries"):
        ads_data = fetch_ads_data(entry)

        if ads_data:
            ads_bibtex, ads_abstract = ads_data

            # Parse the BibTeX string returned by ADS
            ads_db = bibtexparser.loads(ads_bibtex)

            if ads_db.entries:
                ads_entry = ads_db.entries[0]
                # Preserve the original citation key
                ads_entry["ID"] = entry["ID"]

                # Add the abstract if it was found
                if ads_abstract:
                    ads_entry["abstract"] = ads_abstract

                updated_entries.append(ads_entry)
            else:
                # If parsing the ADS bibtex failed, keep the original entry
                updated_entries.append(entry)
        else:
            # If no data was found on ADS, keep the original entry
            updated_entries.append(entry)

        # Be respectful to the ADS API by waiting between requests
        time.sleep(1)

    # Replace the old entries with the updated ones
    bib_database.entries = updated_entries

    # Save the updated database to the output file
    with open(output_file, "w", encoding='utf-8') as f:
        bibtexparser.dump(bib_database, f)

    print(f"\nProcessing complete. Updated BibTeX saved to '{output_file}'.")


def main():
    """Main function to run the script."""
    ads_token = get_ads_token(ADS_TOKEN_FILE)
    if ads_token:
        ads.config.token = ads_token
        update_bibtex_file(INPUT_BIB_FILE, OUTPUT_BIB_FILE)


if __name__ == "__main__":
    main()
