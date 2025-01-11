# 项目目录树生成器

一个简单的 Python 脚本，用于生成项目目录结构的 Markdown 文档。

## 功能特点

- 生成清晰的树形目录结构
- 支持自定义忽略文件/目录
- 输出格式化的 Markdown 文档
- 支持通过 YAML 配置文件进行设置

## 安装依赖

```shell
pip install pyyaml
```

## 使用方法

### 基本使用

```shell
python generate_project_tree.py
```

这将在当前目录生成 `tree.md` 文件。

### 使用配置文件

```shell
python generate_project_tree.py -c config.yaml
```

配置文件示例 (config.yaml):
```yaml
ignore_patterns:
  - node_modules
  - .git
  - dist
  - build
  # 添加其他要忽略的文件/目录
```

### 自定义选项

```shell
python generate_project_tree.py -p /path/to/project -o output.md
```

参数说明:
- `-p, --path`: 指定项目根目录路径（默认为当前目录）
- `-o, --output`: 指定输出文件名（默认为 tree.md）
- `-c, --config`: 指定配置文件路径

## 输出示例

```
project_name
├── src
│   ├── main.py
│   └── utils.py
├── tests
│   └── test_main.py
└── README.md
```

## 许可证

MIT License