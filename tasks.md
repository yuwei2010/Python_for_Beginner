# Tasks — File Manager Project

## Task 1 — 创建 data 文件夹
**Goal:** 确保项目中存在 `data/` 文件夹  
**Inputs:** 无  
**Outputs:** 创建目录  
**Checks:**  
- 若目录存在则跳过  
- 若不存在则创建成功  

---

## Task 2 — 生成 5 个文本文件
**Goal:** 创建 `file1.txt` 至 `file5.txt`  
**Inputs:** 文件名列表  
**Outputs:** 5 个空文本文件  
**Checks:**  
- 文件成功创建  
- 文件路径正确  

---

## Task 3 — 写入表格数据
**Goal:** 为每个文件写入包含三列的数据（编号/名称/描述）  
**Inputs:** 文件路径  
**Outputs:** 每个文件包含多行虚拟表格数据  
**Checks:**  
- 文件非空  
- 至少包含 3 列内容  

---

## Task 4 — 读取文件内容并输出
**Goal:** 控制台输出文件名 + 文件内容  
**Inputs:** data 文件夹中的文本文件  
**Outputs:** 标准输出  
**Checks:**  
- 每个文件都有标题输出  
- 内容逐行打印  

---

## Task 5 — 提取名称列
**Goal:** 从所有文件的表格中解析“名称”列  
**Inputs:** 文件内容  
**Outputs:** 名称列表  
**Checks:**  
- 每个文件至少提取 1 条名称  
- 名称字段不为空  

---

## Task 6 — 生成 summary.txt
**Goal:** 将所有名称写入 summary.txt  
**Inputs:** 名称列表  
**Outputs:** summary.txt  
**Checks:**  
- 文件生成成功  
- 内容格式正确（每行一个名称）  
- UTF-8 编码  
