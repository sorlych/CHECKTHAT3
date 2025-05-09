import requests
train_url = "https://gitlab.com/checkthat_lab/clef2025-checkthat-lab/-/raw/main/task2/data/train/train-eng.csv?inline=false"
dev_url = "https://gitlab.com/checkthat_lab/clef2025-checkthat-lab/-/raw/main/task2/data/dev/dev-eng.csv?inline=false"
test_url = "https://gitlab.com/checkthat_lab/clef2025-checkthat-lab/-/raw/main/task2/data/test/test-eng.csv?inline=false"
def download(url, fname):
    get_url = requests.get(url)
    with open(fname, "wb") as f:
        for text in get_url.iter_content(chunk_size=1024):
            if text: 
                f.write(text)
def main():
    # Test, dev and train data
    download(train_url, "train.csv")
    download(dev_url, "dev.csv")
    download(test_url, "test.csv")
if __name__ == "__main__":
    main()