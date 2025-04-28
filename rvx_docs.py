from os_util import *
import argparse
import pypandoc
import zipfile

from bs4 import BeautifulSoup
import html


def convert_terminal_html(html_text: str) -> str:
    soup = BeautifulSoup(html_text, "html.parser")

    for div in soup.find_all("div", class_="tcolorbox"):
        code_tags = div.find_all("code")
        if not code_tags:
            continue

        # 모든 <code> 태그의 내용을 줄바꿈 기준으로 연결
        content = "\n".join(code.get_text().replace("\\\\", "")
                            for code in code_tags).strip()

        # 새 터미널 박스 div 생성
        terminal_div = soup.new_tag("div")
        terminal_div["style"] = (
            "background-color: #1e1e1e; color: #d4d4d4; "
            "font-family: 'Courier New', Courier, monospace; "
            "padding: 0.5em 0.75em; border-radius: 6px; "
            "margin: 1em 0; font-size: 1em; line-height: 1.4;"
        )

        # 코드 삽입 (엔티티 이스케이프 적용)
        code_pre = soup.new_tag("pre", style="margin: 0;")
        code_code = soup.new_tag("code")
        code_code.string = html.escape(content)
        code_pre.append(code_code)
        terminal_div.append(code_pre)

        # 원래 div 교체
        div.replace_with(terminal_div)

    return str(soup)


def convert_gt_in_div_html(html_text: str) -> str:
    soup = BeautifulSoup(html_text, 'html.parser')

    # 모든 <div> 태그를 순회
    for div in soup.find_all('div'):
        original_html = div.decode_contents()
        updated_html = original_html.replace('&amp;gt;', '>')
        div.clear()
        div.append(BeautifulSoup(updated_html, 'html.parser'))

    return str(soup)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='RVX Docs Util')
    parser.add_argument('-cmd', '-c', help='command')
    parser.add_argument('-input', '-i', help='input')
    parser.add_argument('-output', '-o', help='output')
    parser.add_argument('-resource', '-r', help='resource path')
    args = parser.parse_args()

    assert args.cmd
    input_path = None
    if args.input:
        input_path = Path(args.input)
        assert input_path.is_absolute(), input_path
    output_path = None
    if args.output:
        output_path = Path(args.output)
        assert output_path.is_absolute(), output_path
    resource_path = Path(args.resource)
    assert resource_path.is_dir(), resource_path

    if 0:
        pass
    elif args.cmd == 'latex2html':
        input_dir_path = input_path

        input_zip = input_dir_path.parent / f'{input_path.stem}.zip'
        if input_zip.is_file():
            remove_directory(input_dir_path)
            with zipfile.ZipFile(input_zip, 'r') as zip_ref:
                zip_ref.extractall(input_dir_path)

        if input_dir_path.is_dir():
            assert output_path.is_dir(), output_path
            for input_latex_path in input_dir_path.glob(f'{input_path.stem}*.tex'):
                assert input_latex_path.is_file(), input_latex_path
                print(input_latex_path)
                output_html_path = output_path / f'{input_latex_path.stem}.html'

                subprocess.run([
                    'pandoc',
                    str(input_latex_path),
                    '-o', str(output_html_path),
                    '-s',
                    '--mathjax',
                    '--filter', 'pandoc-crossref'
                ], check=True)

                output_text = output_html_path.read_text(encoding='utf-8')
                output_text = convert_terminal_html(output_text)
                output_text = convert_gt_in_div_html(output_text)                
                output_html_path.write_text(output_text, encoding='utf-8')

            figures_src_dir = input_dir_path / 'figures'
            if figures_src_dir.is_dir():
                figures_dst_dir = output_path / 'figures'
                figures_dst_dir.mkdir(parents=True, exist_ok=True)
                for src_file in figures_src_dir.iterdir():
                    if src_file.is_file():
                        dst_file = figures_dst_dir / src_file.name
                        copy_file(src_file, dst_file)

    else:
        assert 0, args.cmd
