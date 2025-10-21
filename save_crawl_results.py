# save_crawl_results.py
import csv, datetime

def save_results(results):
    """Save crawl results to a CSV file with today's date."""
    filename = f"crawl_results_{datetime.date.today()}.csv"
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["URL", "Title", "PreviewText"])
        for u, data in results.items():
            writer.writerow([u, data["title"], data["text"]])
    print(f"\n✅ Crawl results saved to {filename}")


#=======
# Students are instructed to run the following codes on colab.

#from save_crawl_results import #save_results
#save_results(results)

#====
#You (students) should get this below file 
#crawl_results_2025-10-21.csv
