import subprocess
import sys

print("🚀 Starting Books Scraper Project...\n")

python_path = sys.executable  # this ensures venv Python is used

# Step 1: Scraper
print("🔹 Running Scraper...")
subprocess.run([python_path, "scraper.py"])

# Step 2: Cleaning
print("\n🔹 Cleaning Data...")
subprocess.run([python_path, "clean_data.py"])

# Step 3: Analysis
print("\n🔹 Running Analysis...")
subprocess.run([python_path, "analysis.py"])

print("\n✅ Project Completed Successfully!")