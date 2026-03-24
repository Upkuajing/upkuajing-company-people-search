# upkuajing-company-people-search

通过跨境魔方开放平台查询全球企业工商信息和人物数据的 AI Agent Skill。

![upkuajing](upkuajing.png)

## 功能特性

- **公司搜索**：按产品、行业、国家、规模等条件搜索全球公司
- **人物搜索**：按职位、公司、学校等条件搜索关键人物
- **详情获取**：获取公司工商信息和人物详细履历
- **联系方式**：查询邮箱、电话、WhatsApp、社交媒体等联系信息

适用场景：外贸客户开发、背景调查、商务谈判准备、人才寻访、竞品分析。

## Skill 安装

### OpenClaw 安装

1. 复制整个 skill 目录到 OpenClaw 的 skills 目录：
```bash
cp -r upkuajing-company-people-search ~/.openclaw/workspace/skills/
```

2. 或者创建符号链接：
```bash
ln -s /path/to/upkuajing-company-people-search ~/.openclaw/workspace/skills/
```

3. 重启 OpenClaw 使 skill 生效

### Claude Code 安装

1. 复制整个 skill 目录到 Claude Code 的 skills 目录：
```bash
cp -r upkuajing-company-people-search ~/.claude/skills/
```

2. 或者在 Claude Code 设置中配置 skills 路径指向此目录

### 目录结构要求

确保 skill 目录包含以下结构：
```
upkuajing-company-people-search/
├── SKILL.md              # Skill 描述文件（必需）
├── requirements.txt      # Python 依赖
├── scripts/              # Python 脚本目录（必需）
│   ├── auth.py
│   ├── common.py
│   ├── company_list_search.py
│   ├── human_list_search.py
│   ├── company_details.py
│   ├── human_details.py
│   └── get_contact.py
└── references/           # API 参考文档
    ├── company-list-api.md
    ├── human-list-api.md
    ├── company-detail-api.md
    ├── human-detail-api.md
    └── contact-api.md
```

## 环境配置

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 设置 API 密钥

**方式1：使用环境变量**
```bash
export UPKUAJING_API_KEY=your_api_key_here
```

**方式2：使用 .env 文件**
```bash
cp .env.example .env
# 编辑 .env 文件，填入你的 API 密钥
```

### 3. 申请 API 密钥

如果没有 API 密钥，可以通过以下方式申请：
```bash
python scripts/auth.py --new_key
```

## 快速开始

### 在 AI Agent 中使用

安装完成后，可以直接在支持的 AI Agent 工具中使用：

**搜索公司**
```
帮我找生产LED灯的中国厂家，要有邮箱的
```

**搜索人物**
```
找XXXX的CTO
```

**获取详情**
```
获取这个公司的详细信息：[公司ID]
```

### 命令行使用

也可以直接调用 Python 脚本：

```bash
# 公司列表搜索
python scripts/company_list_search.py \
  --params '{"products": ["LED lights"], "countryCodes": ["CN"], "existEmail": 1}' \
  --query_count 20

# 人物列表搜索
python scripts/human_list_search.py \
  --params '{"companyNames": ["XXXX"], "titleRoles": ["CTO"]}' \
  --query_count 20

# 获取公司详情
python scripts/company_details.py --pid [公司ID]

# 获取人物详情
python scripts/human_details.py --hid [人物ID]

# 获取联系方式
python scripts/get_contact.py --bus_id [公司ID或人物ID] --bus_type 1
```

## 使用示例

### 场景1：外贸客户开发

搜索美国电子产品进口商：
```bash
python scripts/company_list_search.py \
  --params '{"products": ["electronics"], "countryCodes": ["US"], "existEmail": 1}' \
  --query_count 50
```

### 场景2：背景调查

获取目标公司的详细信息和联系方式：
```bash
# 先搜索公司
python scripts/company_list_search.py \
  --params '{"companyNames": ["Target Corp"]}' \
  --query_count 10

# 获取详情
python scripts/company_details.py --pid [公司ID]

# 获取联系方式
python scripts/get_contact.py --bus_id [公司ID] --bus_type 1
```

### 场景3：人才寻访

寻找特定职位的关键人物：
```bash
python scripts/human_list_search.py \
  --params '{"titleRoles": ["CEO"], "industries": ["Technology"]}' \
  --query_count 30
```

## API 参考

详细的 API 参数说明请查看 `references/` 目录下的文档：
- [公司列表搜索](references/company-list-api.md)
- [人物列表搜索](references/human-list-api.md)
- [公司详情](references/company-detail-api.md)
- [人物详情](references/human-detail-api.md)
- [联系方式](references/contact-api.md)

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 支持

如有问题或建议，请提交 Issue 或 Pull Request。
