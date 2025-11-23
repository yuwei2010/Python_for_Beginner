"""
File Manager - 自动文件管理工具

本脚本实现以下功能：
1. 创建 data/ 文件夹
2. 生成 5 个文本文件（file1.txt 到 file5.txt）
3. 为每个文件写入包含三列的表格数据（编号、名称、描述）
4. 读取并输出所有文件内容到控制台
5. 从所有文件中提取名称列
6. 将汇总的名称保存到 summary.txt

遵循项目宪章原则：
- 可读性优先
- UTF-8 编码
- 清晰的文档和注释
"""

import os
from pathlib import Path


def create_data_directory():
    """
    Task 1: 创建 data 文件夹
    
    若目录不存在则创建，若存在则跳过
    """
    data_dir = Path("data")
    
    if not data_dir.exists():
        data_dir.mkdir()
        print(f"✓ 已创建目录: {data_dir}")
    else:
        print(f"✓ 目录已存在: {data_dir}")
    
    return data_dir


def create_text_files(data_dir, file_count=5):
    """
    Task 2: 生成指定数量的文本文件
    
    Args:
        data_dir: data 目录路径
        file_count: 要创建的文件数量（默认5个）
    
    Returns:
        文件路径列表
    """
    file_paths = []
    
    for i in range(1, file_count + 1):
        file_path = data_dir / f"file{i}.txt"
        file_paths.append(file_path)
    
    print(f"✓ 准备创建 {file_count} 个文件")
    return file_paths


def write_table_data(file_paths):
    """
    Task 3: 为每个文件写入表格数据
    
    每个文件包含：
    - 表头：编号,名称,描述
    - 5行数据，使用CSV格式（逗号分隔）
    
    Args:
        file_paths: 文件路径列表
    """
    # 定义虚拟数据模板
    names = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    descriptions = [
        "A sweet red fruit",
        "A yellow tropical fruit",
        "A small red stone fruit",
        "A sweet brown fruit from palm trees",
        "A tart dark purple berry"
    ]
    
    for file_path in file_paths:
        with open(file_path, 'w', encoding='utf-8') as f:
            # 写入表头
            f.write("编号,名称,描述\n")
            
            # 写入5行数据
            for i in range(5):
                line = f"{i+1},{names[i]},{descriptions[i]}\n"
                f.write(line)
        
        print(f"✓ 已写入数据到: {file_path.name}")


def read_and_display_files(file_paths):
    """
    Task 4: 读取文件内容并输出到控制台
    
    每个文件输出格式：
    - 文件名作为标题
    - 文件内容逐行打印
    
    Args:
        file_paths: 文件路径列表
    """
    print("\n" + "="*60)
    print("📄 文件内容展示")
    print("="*60 + "\n")
    
    for file_path in file_paths:
        print(f"--- {file_path.name} ---")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
        
        print()  # 空行分隔


def extract_names(file_paths):
    """
    Task 5: 从所有文件中提取名称列
    
    提取规则：
    - 名称在第2列（索引1）
    - 跳过表头行
    - 去除空白字符
    
    Args:
        file_paths: 文件路径列表
    
    Returns:
        名称列表
    """
    all_names = []
    
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            # 跳过表头，从第2行开始
            for line in lines[1:]:
                # 分割CSV行
                columns = line.strip().split(',')
                
                # 提取第2列（名称），去除空白
                if len(columns) >= 2:
                    name = columns[1].strip()
                    if name:  # 确保名称不为空
                        all_names.append(name)
    
    print(f"✓ 共提取 {len(all_names)} 个名称")
    return all_names


def save_summary(names, output_file="summary.txt"):
    """
    Task 6: 保存汇总文件
    
    将所有提取的名称保存到 summary.txt
    - 每行一个名称
    - UTF-8 编码
    - 位于项目根目录
    
    Args:
        names: 名称列表
        output_file: 输出文件名（默认 summary.txt）
    """
    output_path = Path(output_file)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for name in names:
            f.write(f"{name}\n")
    
    print(f"✓ 汇总文件已保存: {output_path}")
    print(f"  包含 {len(names)} 个名称")


def main():
    """
    主函数：按顺序执行所有任务
    """
    print("="*60)
    print("🚀 File Manager 启动")
    print("="*60 + "\n")
    
    # Task 1: 创建 data 目录
    data_dir = create_data_directory()
    
    # Task 2: 生成文件路径
    file_paths = create_text_files(data_dir)
    
    # Task 3: 写入表格数据
    write_table_data(file_paths)
    
    # Task 4: 读取并显示文件
    read_and_display_files(file_paths)
    
    # Task 5: 提取名称列
    names = extract_names(file_paths)
    
    # Task 6: 保存汇总文件
    save_summary(names)
    
    print("\n" + "="*60)
    print("✅ 所有任务完成！")
    print("="*60)


if __name__ == "__main__":
    main()
