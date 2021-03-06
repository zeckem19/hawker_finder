from database import refresh_db_data

from ingest import download_data, extract_data

if __name__ == "__main__":
    download_data()
    data = extract_data()
    refresh_db_data(data)
