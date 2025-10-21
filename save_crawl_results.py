import csv, datetime

filename = f"crawl_results_{datetime.date.today()}.csv"

with open(f"/content/{filename}", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["URL", "Title"])
    for u, t in results.items():
        writer.writerow([u, t])

print(f"✅ Crawl results saved and visible in Colab Files as: {filename}")
