import argparse
import re
from pathlib import Path
import glob
import sys

def flatten_tex(file_path: Path, search_path: Path, seen=None):
    if seen is None:
        seen = set()

    file_path = file_path.resolve()
    if file_path in seen:
        return f"% Skipping already included {file_path}\n"

    seen.add(file_path)

    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        return f"% Error reading {file_path}: {e}\n"

    pattern = re.compile(r'\\input\{([^\}]+)\}')

    def replacer(match):
        subfile = match.group(1)
        subfile_path = search_path / (subfile if subfile.endswith('.tex') else subfile + '.tex')
        print(subfile_path)
        if not subfile_path.exists():
            return f"% File not found: {subfile_path}\n"
        return flatten_tex(subfile_path, search_path, seen)

    return pattern.sub(replacer, content)


def main():
    parser = argparse.ArgumentParser(description="Flatten LaTeX files by expanding all \\input{} commands")
    parser.add_argument('-i', '--input', required=True, help='Input .tex file or glob pattern (e.g., *.tex)')
    parser.add_argument('-o', '--output', required=True, help='Output file or directory')
    parser.add_argument('-p', '--path', required=True, help='Base path to search for \\input files')

    args = parser.parse_args()

    input_pattern = args.input
    output_path = Path(args.output)
    search_path = Path(args.path)

    is_glob = '*' in input_pattern or '?' in input_pattern or '[' in input_pattern
    matched_files = [Path(f) for f in glob.glob(input_pattern)] if is_glob else [Path(input_pattern)]

    # 📌 매칭되는 파일이 없으면 조용히 종료
    if not matched_files:
        return

    if is_glob:
        # 출력 디렉토리가 없으면 만들고, 아니면 그대로
        output_path.mkdir(parents=True, exist_ok=True)

        for file in matched_files:
            merged = flatten_tex(file, search_path)
            output_file = output_path / file.name
            output_file.write_text(merged, encoding='utf-8')

    else:
        merged = flatten_tex(matched_files[0], search_path)
        output_path.write_text(merged, encoding='utf-8')


if __name__ == '__main__':
    main()
