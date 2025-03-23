# Convert data.json to UTF-8
with open('data.json', 'rb') as f:
    content = f.read()

# Detect encoding (you may need to install `chardet` for this)
try:
    import chardet
    encoding = chardet.detect(content)['encoding']
    print(f"Detected encoding: {encoding}")
except ImportError:
    encoding = 'utf-8'  # Fallback to UTF-8 if chardet is not installed

# Decode and re-encode as UTF-8
decoded_content = content.decode(encoding)
with open('data_utf8.json', 'w', encoding='utf-8') as f:
    f.write(decoded_content)

print("File converted to UTF-8: data_utf8.json")