import argparse
from pathlib import Path
import zipfile
import shutil
import sys

def unzip_tex(zip_path: Path):
    if not zip_path.exists() or not zip_path.is_file():
        return  # zip 파일 없으면 조용히 종료

    # 압축 해제 대상 디렉토리: zip 파일 이름과 같은 이름의 디렉토리
    extract_dir = zip_path.with_suffix('')  # e.g. foo.zip → foo/

    # 디렉토리가 이미 존재하면 삭제
    if extract_dir.exists() and extract_dir.is_dir():
        shutil.rmtree(extract_dir)

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
    except zipfile.BadZipFile:
        print(f"[ERROR] Not a valid zip file: {zip_path}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="Unzip .zip file into named directory (cleaned first if exists)")
    parser.add_argument('-i', '--input', required=True, help='Path to .zip file')

    args = parser.parse_args()
    zip_path = Path(args.input)

    unzip_tex(zip_path)

if __name__ == '__main__':
    main()