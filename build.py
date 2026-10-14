# Rebuilds index.html from template.html with the current wardrobe-cli sources.
# Usage: python3 build.py
import glob, json, os

here = os.path.dirname(os.path.abspath(__file__))
project = os.path.join(here, "..", "wardrobe-cli")
sources = {}
for path in sorted(glob.glob(os.path.join(project, "src", "wardrobe", "*.java"))
                   + glob.glob(os.path.join(project, "tests", "wardrobe", "*.java"))):
    with open(path, encoding="utf-8") as f:
        sources[os.path.basename(path)] = f.read()

with open(os.path.join(here, "template.html"), encoding="utf-8") as f:
    template = f.read()
data = json.dumps(sources, ensure_ascii=False).replace("</", "<\\/")
with open(os.path.join(here, "index.html"), "w", encoding="utf-8") as f:
    f.write(template.replace("__SOURCES_JSON__", data))
print(f"index.html rebuilt with {len(sources)} source files")
