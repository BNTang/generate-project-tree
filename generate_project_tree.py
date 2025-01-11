import argparse
from pathlib import Path
import yaml
from typing import List, Optional

class ProjectTreeGenerator:
    def __init__(self, ignore_patterns: Optional[List[str]] = None):
        # 默认忽略的文件和目录
        self.ignore_patterns = ignore_patterns or [
            "node_modules",
            ".git",
            ".next",
            ".contentlayer",
            ".husky",
            "packages",
            ".vscode",
            ".turbo",
            "tests",
            "ui",
            "public",
            "LICENSE",
            "test.http"
        ]

    def should_include(self, path: Path) -> bool:
        """检查是否应该包含该路径"""
        return path.name not in self.ignore_patterns

    def generate_tree(self, directory: Path, prefix: str = "") -> str:
        """递归生成树状结构"""
        output = []
        directory = Path(directory)
        
        # 获取并过滤目录内容
        items = [x for x in directory.iterdir() if self.should_include(x)]
        items.sort(key=lambda x: x.name.lower())
        
        for i, item in enumerate(items):
            is_last = i == len(items) - 1
            connector = "└── " if is_last else "├── "
            output.append(f"{prefix}{connector}{item.name}")
            
            if item.is_dir():
                new_prefix = prefix + ("    " if is_last else "│   ")
                output.append(self.generate_tree(item, new_prefix))
        
        return "\n".join(output)

    def save_tree(self, root_path: Path, output_file: str):
        """保存目录树到文件"""
        root_path = Path(root_path).resolve()
        tree_content = f"# Project Structure\n\n{root_path.name}\n"
        tree_content += self.generate_tree(root_path)
        
        # 使用 UTF-8 编码保存文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(tree_content)
        
        print(f"✅ 项目结构已保存到 {output_file}")

def main():
    parser = argparse.ArgumentParser(description='生成项目目录树')
    parser.add_argument('-p', '--path', default='.', help='项目根目录路径')
    parser.add_argument('-o', '--output', default='tree.md', help='输出文件路径')
    parser.add_argument('-c', '--config', help='配置文件路径（YAML格式）')
    args = parser.parse_args()

    # 读取配置文件（如果有）
    ignore_patterns = None
    if args.config:
        with open(args.config, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            ignore_patterns = config.get('ignore_patterns')

    generator = ProjectTreeGenerator(ignore_patterns)
    generator.save_tree(args.path, args.output)

if __name__ == '__main__':
    main()