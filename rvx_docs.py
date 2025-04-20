import argparse
import pypandoc
import zipfile

from os_util import *

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
        assert input_dir_path.is_dir(), input_dir_path

        input_zip = input_dir_path.parent / f'{input_path.stem}.zip'
        if input_zip.is_file():
            remove_directory(input_dir_path)
            with zipfile.ZipFile(input_zip, 'r') as zip_ref:
                zip_ref.extractall(input_dir_path)

        assert output_path.is_dir(), output_path
        for input_latex_path in input_dir_path.glob('*.tex'):
            assert input_latex_path.is_file(), input_latex_path
            print(input_latex_path)
            output_text = pypandoc.convert_text(input_latex_path.read_text(encoding='utf-8'), 'html', format='latex', extra_args=[
                                                '-s', '--mathjax',
                                                f'--lua-filter={str(resource_path)}/colorbox.lua',
                                                f'--lua-filter={str(resource_path)}/tcolorbox.lua'
                                                ])
            output_html_path = output_path / f'{input_latex_path.stem}.html'
            output_html_path.write_text(output_text, encoding='utf-8')

        figures_src_dir = input_latex_path.parent / 'figures'

        if figures_src_dir.is_dir():
            figures_dst_dir = output_path / 'figures'
            figures_dst_dir.mkdir(parents=True, exist_ok=True)
            for src_file in figures_src_dir.iterdir():
                if src_file.is_file():
                    dst_file = figures_dst_dir / src_file.name
                    copy_file(src_file, dst_file)

    else:
        assert 0, args.cmd
