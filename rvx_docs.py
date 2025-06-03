from os_util import *
import argparse
import pypandoc
import zipfile

from bs4 import BeautifulSoup
import html


def convert_terminal_html(html_text: str) -> str:
    soup = BeautifulSoup(html_text, "html.parser")

    for div in soup.find_all("div", class_="tcolorbox"):
        p = div.find("p")
        if not p:
            continue

        # 줄 단위로 구성
        lines = []
        buffer = ""

        for elem in p.children:
            if elem.name == "br":
                if buffer.strip():
                    lines.append(buffer.strip())
                buffer = ""
            elif hasattr(elem, "get_text"):
                buffer += elem.get_text()
            else:
                buffer += str(elem)

        if buffer.strip():
            lines.append(buffer.strip())

        content = "\n".join(lines)

        # 새 터미널 div 생성
        terminal_div = soup.new_tag("div")
        terminal_div["style"] = (
            "background-color: #1e1e1e; color: #d4d4d4; "
            "font-family: 'Courier New', Courier, monospace; "
            "padding: 0.5em 0.75em; border-radius: 6px; "
            "margin: 1em 0; font-size: 1em; line-height: 1.4;"
        )

        code_pre = soup.new_tag(
            "pre", style="margin: 0; white-space: pre-wrap;")
        code_code = soup.new_tag("code")
        code_code.string = content
        code_pre.append(code_code)
        terminal_div.append(code_pre)

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

        if input_dir_path.is_dir():
            assert output_path.is_dir(), output_path
            for input_latex_path in input_dir_path.glob(f'{input_path.stem}*.tex'):
                assert input_latex_path.is_file(), input_latex_path
                print(input_latex_path)
                output_html_path = output_path / \
                    f'{input_latex_path.stem}.html'

                output_text = pypandoc.convert_text(
                    input_latex_path.read_text(encoding='utf-8'),
                    'html', format='latex',
                    extra_args=[
                        '-s',
                        '--mathjax',
                        '--filter=pandoc-crossref'
                    ]
                )

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
