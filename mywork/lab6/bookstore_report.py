import os
from pymongo import MongoClient

MONGODB_ATLAS_URL = os.getenv("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.getenv("MONGODB_ATLAS_PWD")


def main():
    client = MongoClient(
        MONGODB_ATLAS_URL,
        username=MONGODB_ATLAS_USER,
        password=MONGODB_ATLAS_PWD
    )

    try:
        db = client["bookstore"]
        collection = db["authors"]

        total_authors = collection.count_documents({})
        print(f"Total number of authors: {total_authors}")
        print()

        authors = collection.find({}, {"_id": 0, "name": 1, "nationality": 1, "birthday": 1, "bio.short": 1})

        for author in authors:
            name = author.get("name")
            nationality = author.get("nationality")
            birthday = author.get("birthday")

            bio = author.get("bio", {})
            short_bio = bio.get("short")

            print(f"Name: {name}")
            print(f"Nationality: {nationality}")
            print(f"Birthday: {birthday}")
            print(f"Short Bio: {short_bio}")
            print()

    finally:
        client.close()


if __name__ == "__main__":
    main()