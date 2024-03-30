def get_materials_link(year):
    links = {
        "1st": {
            "Chem": "https://drive.google.com/file/d/1qW3HksOznsQa8x6BqD9T65Plrg7nHEMi/view?usp=drivesdk",
            "Maths 1": "https://drive.google.com/file/d/1c2pDOdxIRINR2F9uMDmiRqoBP9N59tAQ/view?usp=drivesdk",
            "Physics": "https://drive.google.com/file/d/1DiW9WKHIExHIzqjFHafGwCYUSQgviPK9/view?usp=drivesdk",
            "Maths 2": "https://drive.google.com/file/d/1mGZs0UtgTB-u0fM7jXbA6hXBXE8RqLKs/view?usp=drivesdk",
            "BEE": "https://drive.google.com/file/d/114TBl7IzUZ6e8NYBW2dg9WOSopnmqgNS/view?usp=drivesdk"
        },
        "2nd": {
            "DSA": "https://drive.google.com/file/d/1hbjzGEJp6yjO6ZyB0q3BW8GtZWoJ6wbj/view?usp=drivesdk",
            "OOP": "https://drive.google.com/file/d/1NgQKRKvvqZhSqtPIxJnCotfzLodRtsER/view?usp=drivesdk",
            "PS": "https://drive.google.com/drive/folders/1nkG-x_U3YWQH4nOXihz8UxBNOcPhD1yL",
            "DEC": "https://drive.google.com/file/d/1WkMp7uiAZyGtAlPnisZOSoUZY4ilZPaK/view?usp=drivesdk",
            "DMS": "https://drive.google.com/file/d/16ymXYh_kgg-PHBF7nKF-Rc09HRg2_Ubr/view?usp=drivesdk",
            "AFL": "https://drive.google.com/file/d/1J5KBCvpaIzIJ1OG8w7ZdabyIEI1iZDgx/view?usp=drivesdk",
            "COA": "https://drive.google.com/file/d/1-zLChfky0D7R0cyI6w_f6xvMxxBa7_S0/view?usp=drivesdk",
            "DBMS": "https://drive.google.com/drive/folders/153uOT3OElFpn3yDqmDtEG4m1nVXA4LiK",
            "OS": "https://drive.google.com/drive/folders/18RU3Lb8SZB8CL3qaTcLc1RIOFOPtzuHS",
            "PDC": "https://drive.google.com/drive/folders/18RU3Lb8SZB8CL3qaTcLc1RIOFOPtzuHS"
        },
        "3rd": {
            "HPCA": "https://drive.google.com/drive/folders/1nRYRZ-YOa0XOm_nObk514zbMDfQAm0WO",
            "CN": "https://drive.google.com/drive/folders/1sq1Ys4UsneFhNz4ZRXIeUKsyT8Rv1ngx",
            "DAA": "https://drive.google.com/file/d/1ALRVy5COM0nnv-KAYn5Ku0FO7FS7ac06/view?usp=drivesdk",
            "SE": "https://drive.google.com/drive/folders/1UwEeUYac2fTNGXBWP8Pi28OcHvmuA7d9",
            "CD": "https://drive.google.com/file/d/1i6_hauEfl_lX_WtdW23QlZlcI6HcMHq2/view?usp=drivesdk",
            "AI": "https://drive.google.com/file/d/1BfC0t8Lg1pzc4ggdb75t3FjYenZH0VzG/view?usp=drivesdk",
            "DMDW": "https://drive.google.com/file/d/1Q9NFg4S9rq-7bnR9M65zCQRGqBPUqKo-/view?usp=drivesdk"
        },
        "4th": "https://drive.google.com/file/d/1Q9NFg4S9rq-7bnR9M65zCQRGqBPUqKo-/view?usp=drivesdk"
    }
    return links.get(year, "No materials found for the specified year.")

def material(year):
    links = get_materials_link(year)
    response_message =  ""
    for subject, link in links.items():
        response_message += f"{subject}: {link}\n"
    return response_message