import argparse
import pypandoc

from os_util import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='RVX Docs Util')
    parser.add_argument('-cmd', '-c', help='command')
    parser.add_argument('-input', '-i', help='input')
    parser.add_argument('-output', '-o', help='output')
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

    if 0:
        pass
    elif args.cmd == 'latex2html':
        assert input_path.is_file(), input_path
        assert output_path.is_dir(), output_path
        output_text = pypandoc.convert_text(input_path.read_text(encoding='utf-8'), 'html', format='latex', extra_args=['-s', '--mathjax'])
        output_html_path = output_path / f'{input_path.stem}.html'
        output_html_path.write_text(output_text, encoding='utf-8')
        
        figures_src_dir = input_path.parent / 'figures'
        
        if figures_src_dir.is_dir():
            figures_dst_dir = output_path / 'figures'            
            figures_dst_dir.mkdir(parents=True, exist_ok=True)            
            for src_file in figures_src_dir.iterdir():
                if src_file.is_file():
                    dst_file = figures_dst_dir / src_file.name
                    copy_file(src_file, dst_file)
            
    else:
        assert 0, args.cmd