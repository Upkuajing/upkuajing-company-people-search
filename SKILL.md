---
name: upkuajing-company-people-search
description: 通过跨境魔方开放平台查询企业工商信息和人物数据。支持：搜索全球公司（按产品、行业、国家、规模筛选）；搜索关键人物（按职位、公司、学校筛选）；获取详情（工商信息、教育经历、工作履历）；获取联系方式（邮箱、电话、WhatsApp、社交媒体、网站）。适用场景：外贸客户开发、背景调查、商务谈判准备、人才寻访、竞品分析。
metadata: {"version":"1.0.0","homepage":"https://www.upkuajing.com","clawdbot":{"emoji":"🏢","requires":{"bins":["python"],"env":["UPKUAJING_API_KEY"]},"primaryEnv":"UPKUAJING_API_KEY"}}
---

# 跨境魔方企业与人物搜索

使用跨境魔方开放平台API查询企业工商信息和人物数据。本技能采用**实体驱动方式**：通过公司属性（产品、行业、规模）和人物属性（职位、学校、经历）直接查找目标实体。

## 概述

本技能通过五个脚本提供对跨境魔方全球企业库和人物数据的访问：两种列表搜索（公司、人物）和三个增强接口（公司详情、人物详情、联系方式）。
通过`auth.py`脚本提供 API密钥生成、充值；

## 脚本运行

### 环境准备

1. **检查 Python**：`python --version`
2. **安装依赖**：`pip install -r requirements.txt`

脚本目录：`scripts/*.py`
运行示例：`python scripts/*.py`

### 两种搜索方式

**公司列表搜索** (`company_list_search.py`)
- **返回粒度**：每家公司为一行记录
- **适用场景**：关心的是"有哪些公司"
- **示例**：
   - "找生产LED灯的厂家"
   - "找员工规模100-500人的科技公司"
- **参数**：查看参数说明 [公司列表](references/company-list-api.md)

**人物列表搜索** (`human_list_search.py`)
- **返回粒度**：每个人物为一行记录
- **适用场景**：关心的是"有哪些人"
- **示例**：
  - "找XXXX的CTO"
  - "找XXX中国区的销售总监"
- **参数**：查看参数说明 [人物列表](references/human-list-api.md)

### 三个增强接口

在获取到公司或人物列表后，如有必要，可通过以下接口获取信息增强：

**公司详情** (`company_details.py --pid *`)
- 获取公司工商信息（不包括联系方式）
- **参数**：`--pid` 公司ID（从列表搜索获取）

**人物详情** (`human_details.py --hid *`)
- 获取人物详细信息（教育经历、工作履历等）
- **参数**：`--hid` 人物ID（从列表搜索获取）

**联系方式** (`get_contact.py --bus_id * --bus_type *`)
- 获取联系方式（邮箱、电话、WhatsApp、社媒、网站）
- **参数**：
  - `--bus_id`: 公司ID或人物ID
  - `--bus_type`: 1=公司，2=人物

## API密钥与充值
使用此技能需要API密钥。API密钥应设置在 `UPKUAJING_API_KEY` 环境变量中;
```bash
echo $UPKUAJING_API_KEY
cat ./.env
export UPKUAJING_API_KEY=your_api_key_here
```
### **未设置API密钥**
请先检查`./.env`文件是否有UPKUAJING_API_KEY;
如果未设置UPKUAJING_API_KEY API密钥，请提示并让用户选择：
1. 用户有，由用户提供(让用户设置到环境变量)
2. 用户没有，你可使用接口进行申请（`auth.py --new_key`），申请到新密钥后，需告知用户妥善保存
等待用户选择；

### **账户充值**
如果调用接口响应账户余额不足时，需说明并引导用户进行账户充值：
1. 创建充值订单（`auth.py --new_rec_order`）
2. 根据订单响应，发送支付页面URL给用户，引导用户打开地址付款，付款成功后告诉你；

### **获取账户信息**
可通过此脚本，获取UPKUAJING_API_KEY对应的账户信息 `auth.py --account_info`
  
## 费用

**所有API调用都会产生费用** API调用按请求次数计费。
**最新价格信息**：用户可访问 [详细价格说明](https://www.upkuajing.com/web/openapi/price.html)

在进行多次API调用之前，请告知用户预计费用并获得确认。
**确认规则：只要 query_count > 20，无论请求多少条，执行前必须：**
1. 计算所需调用次数：`ceil(query_count / 20)` 次
2. 告知用户预计消耗次数
3. 等待用户确认后再执行脚本


## 工作流程
根据用户意图选择合适的API。

### 决策指南

| 用户意图 | 使用API |
|-------------|---------|
| "找生产XXX的公司" | 公司列表 |
| "找有邮箱/电话的公司" | 公司列表 existEmail=1/existPhone=1 |
| "找XX公司的CEO/CTO" | 人物列表 |
| "找采购XXX的客户" | 公司列表 |
| "获取人物履历" | 人物详情 |
| "获取联系方式" | 联系方式 |

## 使用示例

### 场景1: 小量查询 — 搜索公司

**用户请求**："找生产LED灯的中国厂家"
```bash
python scripts/company_list_search.py \
  --params '{"products": ["LED lights"], "countryCodes": ["CN"], "existEmail": 1}' \
  --query_count 20
```

### 场景2: 搜索人物

**用户请求**："找XXXX的CTO"
```bash
python scripts/human_list_search.py \
  --params '{"companyNames": ["XXXX"], "titleRoles": ["CTO"]}' \
  --query_count 20
```

### 场景3: 大量查询 — 需要多次调用脚本

**用户请求**："找1000家有邮箱的美国电子产品进口商"
**执行前**告知用户：ceil(1000/20) = 50 次API调用，确认后再执行。
```bash
python scripts/company_list_search.py --params '{"products": ["electronics"], "countryCodes": ["US"], "existEmail": 1}' --query_count 1000
```
**执行结束**：脚本响应 {"task_id":"a1b2-c3d4", "file_url": "xxxxx", ……}
**继续执行，追加数据**：指定task_id，让脚本从上次的cursor处继续查询并追加到文件
```bash
python scripts/company_list_search.py --task_id 'task-id-here' --query_count 2000
```

## 错误处理

- **API密钥无效/不存在**：检查`UPKUAJING_API_KEY`环境变量
- **余额不足**：引导用户充值
- **参数无效**：检查参数名称和值

## 最佳实践

### 选择正确的方法

1. **理解用户意图**：
   - 找公司？ → 使用**公司列表搜索**
   - 找人？ → 使用**人物列表搜索**

2. **优化查询参数**：
   - 使用 `products` 参数精确筛选产品，需翻译为英文
   - 使用 `existEmail=1` 或 `existPhone=1` 筛选有联系方式的实体
   - 使用 `countryCodes` 限定国家范围

### 处理结果

3. **谨慎处理jsonl文件**：对数据量大的查询，注意文件大小
4. **逐步丰富信息**：仅在需要时调用详情/联系接口
   - 两个列表接口返回的公司ID都可以用于两个详情接口
   - 如果用户只需要少数公司，不要为所有公司获取详情

## 注意事项
- 人物搜索用 hid，公司搜索用 pid，注意区分
- 所有时间戳均为毫秒级
- 国家代码使用ISO 3166-1 alpha-2格式（例如：CN、US、JP）
- 文件路径在所有平台上都使用正斜杠
- 产品名称、行业名称需要使用**英文**
- 搜索数量会影响接口的响应时间，建议设置 timeout:120
- **禁止输出技术参数格式**：不要在回复中展示代码样式的参数，应将其转换为自然语言
- **不要**估算、猜测每次调用的费用，如有需要，使用`auth.py --account_info` 获取余额
